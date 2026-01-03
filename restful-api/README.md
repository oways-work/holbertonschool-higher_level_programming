# REST API Project

This project explores the fundamentals of RESTful APIs, including HTTP/HTTPS protocols, API consumption, and development.

## Task 0: Basics of HTTP/HTTPS

### 1. Differences between HTTP and HTTPS

* **HTTP (HyperText Transfer Protocol):**
    * Transmits data in **plaintext**.
    * Vulnerable to eavesdropping; attackers can intercept and read the data.
    * Typically uses port 80.

* **HTTPS (HTTP Secure):**
    * Uses **SSL/TLS encryption** to scramble data during transit.
    * Ensures confidentiality, data integrity, and authentication using digital certificates.
    * Typically uses port 443.

### 2. Structure of HTTP Requests and Responses

#### HTTP Request Structure (Client to Server)
1.  **Start Line:** Contains the Method (e.g., `GET`), Path, and HTTP Version.
2.  **Headers:** Key-value pairs providing metadata (e.g., `Host: example.com`).
3.  **Empty Line:** Separates headers from the body.
4.  **Body (Optional):** Data sent to the server (used in POST/PUT).

#### HTTP Response Structure (Server to Client)
1.  **Status Line:** Contains the HTTP Version, Status Code (e.g., `200`), and Status Message.
2.  **Headers:** Key-value pairs providing metadata (e.g., `Content-Type: application/json`).
3.  **Empty Line:** Separates headers from the body.
4.  **Body (Optional):** The resource content (HTML, JSON, etc.).

### 3. Common HTTP Methods

| Method | Description | Use Case |
| :--- | :--- | :--- |
| **GET** | Retrieves a representation of the specified resource. | Fetching a webpage or user profile. |
| **POST** | Submits data to the specified resource, often causing a state change. | Submitting a form or creating a user. |
| **PUT** | Replaces the target resource with the request payload. | Updating a user's full profile. |
| **DELETE** | Deletes the specified resource. | Removing a post or item. |

### 4. Common HTTP Status Codes

| Code | Description | Scenario |
| :--- | :--- | :--- |
| **200** | **OK** | The request succeeded. |
| **301** | **Moved Permanently** | The URL has changed permanently (redirect). |
| **403** | **Forbidden** | The server refuses to authorize the request. |
| **404** | **Not Found** | The resource does not exist. |
| **500** | **Internal Server Error** | Unexpected server-side error. |

---

## Task 1: Consume data from an API using command line tools (curl)

`curl` is a command-line tool used to transfer data to or from a server. It is essential for debugging and testing APIs.

### 1. Installation & Verification
To verify `curl` is installed and check supported protocols:
```bash
curl --version
