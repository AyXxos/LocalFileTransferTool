# 🌐 Serveur Client-Server Application

A Python-based client-server application with a graphical user interface for Windows clients and a command-line server.

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Configuration](#configuration)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [Security Considerations](#security-considerations)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Client-Server Architecture**: TCP socket communication between client and server
- **GUI Client**: User-friendly Windows interface built with Tkinter
- **Multi-threaded Server**: Handles multiple client connections simultaneously
- **Cross-platform**: Server runs on any Python-supported platform, client designed for Windows
- **Real-time Communication**: Instant message exchange between client and server

## 📦 Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- Network connectivity between client and server machines

## 🚀 Installation

### 1. Clone or Download the Project

```bash
cd "c:\Users\adams\Desktop\PY\Serveur"
```

### 2. Install Python Dependencies

No external dependencies required - uses Python standard library only:
- `socket` - Network communication
- `threading` - Multi-threaded server
- `tkinter` - GUI (included with Python on Windows)

### 3. Verify Python Installation

**Windows**
```bash
python --version
```

**macOS/Linux**
```bash
python3 --version
```

## 📁 Project Structure

```
Serveur/
├── Client/
│   ├── clientWindows.py      # Windows GUI client application
│   └── ...                    # Other client-related files
├── Serveur/
│   └── ...                    # Server implementation files
└── READMe.md                  # This file
```

## 🎯 Usage

### Running the Server

1. Navigate to the server directory:
```bash
cd Serveur
```

2. Start the server:
```bash
python server.py
```

The server will start listening for incoming connections on the configured port (default: usually 5000 or 8080).

### Running the Client (Windows)

1. Navigate to the client directory:
```bash
cd Client
```

2. Launch the Windows client:
```bash
python clientWindows.py
```

3. In the GUI:
   - Enter the server IP address
   - Enter the server port
   - Click "Connect"
   - Start sending and receiving messages

## ⚙️ Configuration

### Server Configuration

Typical server configuration parameters (check server files for exact implementation):

```python
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 5000       # Default port (adjust as needed)
```

### Client Configuration

In the GUI, you'll need to provide:
- **Server IP**: The IP address of the machine running the server
  - For local testing: `127.0.0.1` or `localhost`
  - For network: The actual IP address of the server machine
- **Port**: The port number the server is listening on (must match server configuration)

## 🔧 How It Works

### Server Side

1. **Initialization**: Server binds to specified host and port
2. **Listening**: Waits for incoming client connections
3. **Multi-threading**: Each client connection is handled in a separate thread
4. **Message Handling**: Receives messages from clients and processes them
5. **Broadcasting**: Can send messages to connected clients

### Client Side

1. **GUI Launch**: Tkinter window opens with connection interface
2. **Connection**: User enters server details and establishes TCP connection
3. **Message Exchange**: 
   - Send messages to server through input field
   - Receive and display messages from server
4. **Disconnection**: Clean socket closure when client exits

## 🛠️ Troubleshooting

### Connection Refused

**Problem**: Client cannot connect to server

**Solutions**:
- Verify server is running
- Check firewall settings on both machines
- Ensure correct IP address and port
- For local testing, use `127.0.0.1`

### Port Already in Use

**Problem**: Server won't start - port is occupied

**Solutions**:
```bash
# Windows - Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (use PID from above)
taskkill /PID <PID> /F
```

### Tkinter Not Available

**Problem**: "No module named tkinter"

**Solution**:
- Tkinter should be included with Python on Windows
- If missing, reinstall Python and ensure "tcl/tk and IDLE" is selected during installation

### Network Issues

**Problem**: Cannot connect across network

**Solutions**:
- Check firewall rules (allow Python through firewall)
- Verify both machines are on same network or have proper routing
- Use `ipconfig` (Windows) or `ifconfig` (Linux/Mac) to verify IP addresses

## 🔒 Security Considerations

⚠️ **Important Security Notes**:

1. **No Encryption**: Current implementation likely uses plain TCP without encryption
   - Consider implementing SSL/TLS for production use
   - Use libraries like `ssl` module for secure communication

2. **Authentication**: 
   - No built-in authentication system
   - Add user authentication for production environments

3. **Input Validation**:
   - Always validate and sanitize received data
   - Implement message size limits to prevent DoS attacks

4. **Firewall Configuration**:
   - Only open necessary ports
   - Use firewall rules to restrict access to trusted IPs

5. **Network Exposure**:
   - Avoid exposing server directly to internet without proper security measures
   - Consider using VPN or SSH tunneling for remote connections

## 💡 Development Tips

### Local Testing

For testing on a single machine:
1. Start server with `HOST = 'localhost'`
2. Connect client to `127.0.0.1`
3. Use the same port number for both

### Network Testing

For testing across network:
1. Find server machine's IP address:
   ```bash
   # Windows
   ipconfig
   
   # Linux/Mac
   ifconfig
   ```
2. Configure server to listen on `0.0.0.0`
3. Connect client using server's actual IP address

## 📝 Example Use Cases

- **Chat Application**: Real-time messaging between users
- **File Transfer**: Send files between client and server
- **Remote Command Execution**: Execute commands on server from client
- **Data Monitoring**: Real-time data transmission and display
- **Game Server**: Multiplayer game communication

## 🤝 Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is available for educational and personal use.

## 👤 Author

**AyXxos**

## 📞 Support

For issues, questions, or suggestions, please create an issue in the project repository.

---

⭐ **Note**: This is an educational project. For production use, implement proper security measures, error handling, and testing.
