MAX_VALUE = 5;
INTERVAL = 1000;

class Timer {

    constructor(handler) {
        this.handler = handler;
    }

    genData() {
        let newData = Math.random() * MAX_VALUE;
        this.handler.processReadingOnIoTDevice(newData);
        console.log('New Data: ' + newData);
    }

    start() {
        setInterval(this.genData, INTERVAL);
    }
}

module.exports = Timer;