let ThingSpeakClient = require('thingspeakclient');

CHANNELID = 382493;
ARCHIVELENGTH = 10;

class Handler {
    constructor() {
        this.client = new ThingSpeakClient();
        this.SMA = new Array(ARCHIVELENGTH).fill(0);
        this.client.attachChannel(CHANNELID, {
            writeKey: '5RND6RVZ6PEGVTDD',
            readKey: 'Z9WG7L90VVBL9HG8'
        });
    }

    processReadingOnIoTDevice(newData) {
        let diff = Math.abs(newData - this.SMA.slice(-1).pop());
        if (diff > 0.1) {
            this.client.updateChannel(CHANNELID, newData);
            console.log('Sent new data to ThingSpeak. Difference: ' + diff);
        }
        this.SMA.push(newData);
        this.SMA.shift();

        console.log('Received new Data: ' + newData);
    }

    calcSMA() {

    }

}

module.exports = Handler;