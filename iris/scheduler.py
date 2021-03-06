###########
# IMPORTS #
###########

from heapq import heappop as heap_pop
from heapq import nsmallest as heap_read
from heapq import nlargest

from terminaltables import AsciiTable

import settings
from settings import NODES
import log

#########
# CLASS #
#########

class Scheduler:
    time = 0
    time_previous = 0
    events = []

    def __str__(self):
        lines = ["",
                 Scheduler._get_heap_table(),
                 "",
                 Scheduler._get_status_table()]
        return "\n".join(lines)

    def step():
        # logging
        log.plain("\n")
        log.success("stepping")
        # logging

        packet = heap_pop(Scheduler.events)

        Scheduler.time_previous = Scheduler.time
        Scheduler.time = packet.time

        # this works because the way the list is built introduces a 1:1 relation between the id and the index
        # if the packet was lost (i.e. the queue was full), take no action
        current_node = NODES[packet.sender]
        if not packet.is_queued:
            current_node.generate_next_packet()
        if not packet.is_lost:
            current_node.handle_packet(packet)

        # logging
        log.plain(Scheduler())
        # logging

    def handle_results():
        if settings.FOLDER:
            file_total = open(settings.FOLDER+"/total.csv", "a")
            file_nodes = open(settings.FOLDER+"/nodes.csv", "a")

        results_title = log.format_color("results", "green")
        results_data = [["NODE", "THROUGHPUT (kB/s)", "COLLISION RATE (%)", "LOSS RATE (%)", "generated"]]

        loss_rate_total = 0
        collision_rate_total = 0
        throughput_total = 0
        # exponential scale is the mean of an exponential distribution https://www.johndcook.com/blog/2010/02/03/statistical-distributions-in-scipy/
        # mean of the size of each single packet divided by the mean of the inter arrival time
        average_load = ((settings.UNIFORM_MAX-settings.UNIFORM_MIN)/2) / (settings.GAMMA_SHAPE*settings.GAMMA_SCALE)  # mean of the size of each single packet divided by the mean of the inter arrival time
        for node in NODES:
            throughput = node.data_sent/nlargest(1, Scheduler.events)[0].time # data_sent/last absolute time # mean of data sent per second
            throughput_total += throughput
            loss_rate = node.packets_lost/node.packets_generated
            loss_rate_total += loss_rate
            try:
                collision_rate = node.packets_collided/(node.packets_received+node.packets_collided)
            except ZeroDivisionError:
                collision_rate = 0
            collision_rate_total += collision_rate

            line = [str(node.id), settings.PRECISION.format(throughput/1000), settings.PRECISION.format(collision_rate*100), settings.PRECISION.format(loss_rate*100), settings.PRECISION.format(node.packets_generated)]
            results_data.append(line)
            if settings.FOLDER:
                file_nodes.write(",".join([str(node.id), settings.PRECISION.format(settings.GAMMA_SCALE), settings.PRECISION.format(throughput), settings.PRECISION.format(average_load), settings.PRECISION.format(collision_rate*100), settings.PRECISION.format(loss_rate*100)]))
                file_nodes.write("\n")

        line = ["MEAN", settings.PRECISION.format(throughput_total/1000/len(NODES)), settings.PRECISION.format(collision_rate_total/len(NODES)*100), settings.PRECISION.format(loss_rate_total/len(NODES)*100)]
        results_data.append(line)
        if settings.FOLDER:
            file_total.write(",".join([settings.PRECISION.format(settings.GAMMA_SCALE), settings.PRECISION.format(throughput_total/len(NODES)), settings.PRECISION.format(average_load), settings.PRECISION.format(collision_rate_total/len(NODES)*100), settings.PRECISION.format(loss_rate_total/len(NODES)*100)]))
            file_total.write("\n")

        if not settings.QUIET:
            print("\n")
            print(AsciiTable(results_data, results_title).table)
            print("\n")
            print(" ".join(["SYSTEM THROUGHPUT (kB/s) =", settings.PRECISION.format(throughput_total/1000)]))

        if settings.FOLDER:
            file_nodes.close()
            file_total.close()

    def _get_heap_table():
        heap_title = log.format_color("events", "green")
        heap_data = [["TIME", "NODE", "PACKET"]]

        ordered_events = heap_read(len(Scheduler.events), Scheduler.events)
        for packet in ordered_events:
            if packet.time == Scheduler.time:
                time = log.format_evidence(settings.PRECISION.format(packet.time), "yellow")
            else:
                time = settings.PRECISION.format(packet.time)

            heap_data.append([time, str(packet.sender), str(packet.id)])

        return AsciiTable(heap_data, heap_title).table

    def _get_status_table():
        status_title = log.format_color(" ".join(["time =", settings.PRECISION, "s(abs)"]).format(Scheduler.time), "green")
        status_data = [["NODE", "STATUS", "QUEUE", "TO", "FOR s(rel)", "UNTIL s(abs)", "LOST", "SENT", "RECEIVED", "COLLIDED"]]

        for node in NODES:
            if node.is_idle():
                status = log.format_evidence("IDLE", "green")
                time_relative = "-"
                time_absolute = "-"
            elif node.is_sending():
                status = log.format_evidence("SENDING", "cyan")
                time_relative = settings.PRECISION.format(node.sending_until-Scheduler.time)
                time_absolute = settings.PRECISION.format(node.sending_until)
            elif node.is_receiving():
                status = log.format_evidence("RECEIVING", "magenta")
                time_relative = settings.PRECISION.format(node.receiving_until-Scheduler.time)
                time_absolute = settings.PRECISION.format(node.receiving_until)

            destinations = []
            for neighbour in node.neighbours:
                destinations.append(neighbour.id)

            queued = []
            for packet in node.queue:
                queued.append(packet.id)

            status_data.append([str(node.id), status, str(queued), str(destinations), time_relative, time_absolute, str(node.packets_lost), str(node.packets_sent), str(node.packets_received), str(node.packets_collided)])

        return AsciiTable(status_data, status_title).table
