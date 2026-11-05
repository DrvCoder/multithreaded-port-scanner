# Multi-Threaded TCP Port Scanner

A fast, lightweight, and concurrent TCP port scanner utility engineered in Python. Designed to identify open ports and active services on a target network host utilizing multi-threading for optimized execution speed.

## Features

- **Concurrent Execution:** Leverages Python's `concurrent.futures.ThreadPoolExecutor` to query up to 100 ports simultaneously, drastically reducing execution time compared to sequential scanning.
- **Low Dependencies:** Built entirely using Python's standard library (`socket`, `concurrent.futures`), requiring no external third-party package installations.
- **Robust Error Handling:** Gracefully handles socket timeouts, network unreachability, and user interruptions (`KeyboardInterrupt`).
- **Configurable Timeout:** Implements strict connection timeouts to prevent hanging threads on filtered or unresponsive ports.

## Prerequisites

- Python 3.x installed on your local machine.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/DrvCoder/multithreaded-port-scanner.git](https://github.com/DrvCoder/multithreaded-port-scanner.git)
   cd multithreaded-port-scanner