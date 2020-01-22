const { exec, execFile } = require('child_process');
const fs = require('fs');
const net = require('net');

const IMAGE_PATH = 'images/tmp.png';
const HOST = 'localhost';
const PORT = 3001;
const begin = Date.now();
const debugging = false;

const sleep = ms => {
    return new Promise(resolve => setTimeout(resolve, ms));
};

const debug = msg => {
    if (debugging) {
        console.log(msg);
    }
};

const doAction = action => {
    console.log(action);

    switch (action) {
        case 'Play':
            execFile('osascript', ['scripts/play.scpt']);
            break;
        case 'Pause':
            execFile('osascript', ['scripts/pause.scpt']);
            break;
        case 'Next Track':
            execFile('osascript', ['scripts/nextTrack.scpt']);
            break;
        case 'Previous Track':
            execFile('osascript', ['scripts/previousTrack.scpt']);
            break;
        case 'Volume Up':
            execFile('osascript', ['scripts/volumeUp.scpt']);
            break;
        case 'Volume Down':
            execFile('osascript', ['scripts/volumeDOwn.scpt']);
            break;
        case 'Undefined':
            break;
        default:
    }
};

const doDetection = () => {
    return new Promise((resolve, reject) => {
        const client = new net.Socket();

        client.connect(PORT, HOST, () => {
            client.write('../images/tmp.png');
        });

        client.on('data', data => {
            const action = data.toString();
            doAction(action);
            client.destroy();
            fs.unlinkSync(IMAGE_PATH);
            resolve();
        });

        client.on('error', () => {
            client.destroy();
            fs.unlinkSync(IMAGE_PATH);
            resolve();
        });
    });
};

const doCapture = async () => {
    return new Promise(async (resolve, reject) => {
        exec(`imagesnap ${IMAGE_PATH}`);

        await new Promise(async (resolve, reject) => {
            while (true) {
                await sleep(100);

                if (false === fs.existsSync(IMAGE_PATH)) {
                    continue;
                }

                break;
            }

            resolve();
        });

        debug(`doDetection - ${Date.now() - begin}`);
        await doDetection();
        debug(`doDetection end - ${Date.now() - begin}`);
        resolve();
    });
};

(async () => {
    while (1) {
        debug(`doCapture - ${Date.now() - begin}`);
        await doCapture();
        debug(`doCapture end - ${Date.now() - begin}`);
    }
})();
