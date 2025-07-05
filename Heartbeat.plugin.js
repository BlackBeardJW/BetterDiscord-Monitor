/**
 * @name Heartbeat
 * @author You
 * @version 1.0.0
 * @description Writes a heartbeat file every 10 seconds so external scripts can monitor BD status.
 */

const fs = require("fs");
const path = require("path");

class Heartbeat {
    start() {
        this._running = true;
        this._heartbeatFile = path.join(__dirname, "bd_heartbeat.txt");
        this._loop();
        BdApi.showToast("Heartbeat plugin started.", {type: "info"});
    }

    stop() {
        this._running = false;
        BdApi.showToast("Heartbeat plugin stopped.", {type: "info"});
    }

    _loop() {
        if (!this._running) return;
        const timestamp = new Date().toLocaleString('sv-SE').replace(' ', 'T');
        fs.writeFileSync(this._heartbeatFile, timestamp);
        setTimeout(() => this._loop(), 10 * 1000); // every 10 sec
    }
}

