let ThingSpeakClient = require('thingspeakclient');

ArchiveLength = 10;
Threshold_Simple = 0.1;
Threshold_SMA = 0.5;

ChannelId = 382493;
KeyWrite = '5RND6RVZ6PEGVTDD';
KeyRead = 'Z9WG7L90VVBL9HG8';

ModeSMA = true;

class Handler {
    constructor() {
        this.client = new ThingSpeakClient();
        this.SMA = new Array(ArchiveLength).fill(0);
        this.lastAverageSent = 0;

        this.client.attachChannel(ChannelId, {
            writeKey: KeyWrite,
            readKey: KeyRead
        });
    }

    processReadingOnIoTDevice(newData) {
        console.log('Received new Data: ' + newData);

        let result = ModeSMA ? this.calcSMA(newData) : this.calcSimple(newData);

        if (result.above_threshold)
            this.sendToEdgeNode(result.dataToSent);
    }

    calcSMA(newData) {
        this.SMA.shift();
        this.SMA.push(newData);

        let newAverage = this.SMA.reduce((p, c) => p + c, 0) / this.SMA.length;
        let diff = Math.abs(newAverage - this.lastAverageSent);
        let above_threshold = diff > Threshold_SMA;

        if (above_threshold)
            this.lastAverageSent = newAverage;

        return {above_threshold: above_threshold, dataToSent: newAverage}
    }

    calcSimple(newData) {
        let lastData = this.SMA.slice(-1).pop();
        let diff = Math.abs(newData - lastData);
        let above_threshold = diff > Threshold_Simple;

        return {above_threshold: above_threshold, dataToSent: newData}
    }

    sendToEdgeNode(data) {
        let fieldDict = {field1: data};

        this.client.updateChannel(ChannelId, fieldDict, function (result) {
            if (result !== null) {
                console.error('Data could not be sent. Error: ' + result.message)
            } else {
                console.log('Data sent to ThingSpeak: ' + data)
            }
        });
    }
}

module.exports = Handler;