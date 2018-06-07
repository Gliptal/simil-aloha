#----------#
# PLOTTING #
#----------#

plot.new = function() {
    dev.new(width  = 16,
            height =  9)
    par(cex      = 0.6,
        cex.main = 3.0,
        cex.lab  = 3.0,
        cex.axis = 3.0,
        lwd      = 1.2,
        mar      = c(6.0, 7.2, 6.0, 3.0),
        bty      = "n")
}

plot.scale = function(xData, yData) {
    xLab = "scale"
    yLab = "load (%)"

    plot.new()
    plot(xData, yData/PERCENT, type="l", log="x", xlab=xLab, ylab=yLab, xaxt="n", xaxs="i", yaxs="i", xlim=c(10^-3.2, 0.1), ylim=c(0, 100))
    axis(side=1, at=c(0, round(10^-3, 4), round(10^-2.5, 4), round(10^-2, 4), round(10^-1.5, 4), round(10^-1, 4)))
}

plot.throughput = function(xData, yData) {
    xLab = "load (%)"
    yLab = "correct throughput (%)"

    plot.new()
    plot(xData/PERCENT, yData/PERCENT, type="l", xlab=xLab, ylab=yLab, xaxt="n", yaxt="n", xaxs="i", yaxs="i", xlim=c(0, 100), ylim=c(0, 14))
    axis(side=1, at=seq(0, 100, 20))
    axis(side=2, at=seq(0, 14, 2))
}

plot.relativethroughput = function(xData, yData) {
    xLab = "load (%)"
    yLab = "correct throughput (relative %)"

    plot.new()
    plot(xData/PERCENT, (yData/PERCENT)*(100/(xData/PERCENT)), type="l", xlab=xLab, ylab=yLab, xaxt="n", yaxt="n", xaxs="i", yaxs="i", xlim=c(0, 100), ylim=c(0, 100))
    axis(side=1, at=seq(0, 100, 20))
    axis(side=2, at=seq(0, 100, 20))
}

plot.packets = function(xData, yData1, yData2) {
    xLab = "load (%)"
    yLab = "packets collided (%)"

    plot.new()
    plot(xData/PERCENT, yData1, type="l", xlab=xLab, ylab=yLab, xaxt="n", yaxt="n", xaxs="i", yaxs="i", xlim=c(0, 100), ylim=c(0, 100))
    axis(side=1, at=seq(0, 100, 20))
    axis(side=2, at=seq(0, 100, 20))
}

plot.decision = function(xData, yData) {
    xLab = "packets collided (%)"
    yLab = "correct throughput (%)"

    plot.new()
    plot(xData, yData/PERCENT, type="l", xlab=xLab, ylab=yLab, xaxt="n", yaxt="n", xaxs="i", yaxs="i", xlim=c(0, 100), ylim=c(0, 14))
    axis(side=1, at=seq(0, 100, 20))
    axis(side=2, at=seq(0, 14, 2))
}

plot.node = function(xData, yData1, yData2, node) {
    xLab = "load (%)"
    yLab = "packets collided (%)"

    plot.new()
    plot(xData/PERCENT, yData1, type="l", xlab=xLab, ylab=yLab, xaxt="n", yaxt="n", xaxs="i", yaxs="i", xlim=c(0, 100), ylim=c(0, 100))
    axis(side=1, at=seq(0, 100, 20))
    axis(side=2, at=seq(0, 100, 20))
}

boxplot.throughput = function(data) {
    xLab = "load (%)"
    yLab = "correct throughput (%)"

    data$throughput = data$throughput/PERCENT
    data$load = data$load/PERCENT

    plot.new()
    boxplot(throughput ~ load, data=data, at=sort(unique(data$load)), boxwex=1.2, xlab=xLab, ylab=yLab, xaxt="n", yaxt="n", xaxs="i", yaxs="i", xlim=c(0, 100), ylim=c(0, 14))
    axis(side=1, at=seq(0, 100, 20))
    axis(side=2, at=seq(0, 14, 2), pos=0.1)
}

boxplot.packets = function(data) {
    xLab = "load (%)"
    yLab = "packets collided (%)"

    data$load = data$load/PERCENT

    plot.new()
    boxplot(collision ~ load, data=data, at=sort(unique(data$load)), boxwex=1.2, xlab=xLab, ylab=yLab, xaxt="n", yaxt="n", xaxs="i", yaxs="i", xlim=c(0, 100), ylim=c(0, 100))
    axis(side=1, at=seq(0, 100, 20))
    axis(side=2, at=seq(0, 100, 20), pos=0.1)
}

boxplot.node = function(data, node) {
    xLab = "load (%)"
    yLab = "packets collided (%)"

    data$load = data$load/PERCENT

    plot.new()
    boxplot(collision ~ load, data=data, at=sort(unique(data$load)), xlab=xLab, ylab=yLab, xaxt="n", yaxt="n", xaxs="i", yaxs="i", xlim=c(0, 100), ylim=c(0, 100))
    axis(side=1, at=seq(0, 100, 20))
    axis(side=2, at=seq(0, 100, 20), pos=0.1)
}

plot.model.throughput = function(model, simulator) {
    xLab = "load (%)"
    yLab = "correct throughput (%)"
    colors = c("gray0", "gray")
    legend = c("model", "simulator")

    plot.new()
    plot(model$load/PERCENT, model$prob, xlab=xLab, ylab=yLab, type="l", col=colors[1], xaxt="n", yaxt="n", xaxs="i", yaxs="i", xlim=c(0, 100), ylim=c(0, 14))
    lines(simulator$load/PERCENT, simulator$throughput/PERCENT, col=colors[2])
    axis(side=1, at=seq(0, 100, 20))
    axis(side=2, at=seq(0, 14, 2))
    legend("topright", legend=legend, lty=c(1, 1), col=colors, bty="n", cex=2.4)
}


#----------#
# SETTINGS #
#----------#

ANALYSE_SYSTEM = TRUE
ANALYSE_NODES  = TRUE
ANALYSE_MODEL  = TRUE

SPEED   = 1000000
PERCENT = SPEED/100


#------#
# MAIN #
#------#

total.data = read.csv("./data/total.csv")
sets = aggregate(total.data[2:5], list(scale=total.data$scale), mean)

if (ANALYSE_SYSTEM) {
    plot.scale(sets$scale, sets$load)
    dev.copy2pdf(file="./graphs/scale.pdf",         width=18, height=10.5)
    plot.relativethroughput(sets$load, sets$throughput)
    dev.copy2pdf(file="./graphs/relative.pdf",      width=18, height=10.5)
    plot.throughput(sets$load, sets$throughput)
    dev.copy2pdf(file="./graphs/throughput.pdf",    width=18, height=10.5)
    boxplot.throughput(total.data)
    dev.copy2pdf(file="./graphs/throughputbar.pdf", width=18, height=10.5)
    plot.packets(sets$load, sets$collision, sets$lost)
    dev.copy2pdf(file="./graphs/packets.pdf",       width=18, height=10.5)
    boxplot.packets(total.data)
    dev.copy2pdf(file="./graphs/packetsbar.pdf",    width=18, height=10.5)
    plot.decision(sets$collision, sets$throughput)
    dev.copy2pdf(file="./graphs/decision.pdf",      width=18, height=10.5)
}

if (ANALYSE_NODES) {
    nodes.data = read.csv("./data/nodes.csv")
    nodes = split(nodes.data, nodes.data$node)
    index = 1
    for (node in nodes) {
        set = aggregate(node[1:6], list(scale=node$scale), mean)

        plot.node(set$load, set$collision, set$lost, set$node[1])
        dev.copy2pdf(file=paste0("./graphs/node", index, ".pdf"),    width=18, height=10.5)
        boxplot.node(node, set$node[1])
        dev.copy2pdf(file=paste0("./graphs/node", index, "bar.pdf"), width=18, height=10.5)
        index = index + 1
    }
}

if (ANALYSE_MODEL) {
    model.data = read.csv('./data/model.csv')
    model.data = aggregate(.~state+load, model.data, sum)

    collision_rate = split(model.data, model.data$state)[['c']]
    transmission_rate = split(model.data, model.data$state)[['t']]

    transmission_rate$prob = transmission_rate$prob*(transmission_rate$load/PERCENT)

    plot.model.throughput(transmission_rate, sets)
    dev.copy2pdf(file=paste0("./graphs/modelthroughput.pdf"), width=18, height=10.5)
}
