# REST API Project

This project explores the fundamentals of RESTful APIs, including HTTP/HTTPS protocols, API consumption, and development using Python.

## Task 0: Basics of HTTP/HTTPS

### 1. Differences between HTTP and HTTPS

* **HTTP (HyperText Transfer Protocol):**
    * Transmits data in **plaintext**.
    * Vulnerable to eavesdropping; attackers can intercept and read the data (e.g., passwords).
    * Typically uses port 80.

* **HTTPS (HTTP Secure):**
    * Uses **SSL/TLS encryption** to scramble data during transit.
    * Ensures confidentiality, data integrity, and authentication using digital certificates.
    * Typically uses port 443.

---

### 2. Structure of HTTP Requests and Responses

#### HTTP Request Structure (Client to Server)
1.  **Start Line:** Contains the Method (e.g., `GET`), Path (e.g., `/index.html`), and HTTP Version.
2.  **Headers:** Key-value pairs providing metadata (e.g., `Host: example.com`, `User-Agent: Mozilla/5.0`).
3.  **Empty Line:** Separates headers from the body.
4.  **Body (Optional):** Data sent to the server (used in POST/PUT).

#### HTTP Response Structure (Server to Client)
1.  **Status Line:** Contains the HTTP Version, Status Code (e.g., `200`), and Status Message (e.g., `OK`).
2.  **Headers:** Key-value pairs providing metadata (e.g., `Content-Type: application/json`).
3.  **Empty Line:** Separates headers from the body.
4.  **Body (Optional):** The resource content (HTML, JSON, image, etc.).

---

### 3. Common HTTP Methods

| Method | Description | Use Case |
| :--- | :--- | :--- |
| **GET** | Retrieves a representation of the specified resource. Should not modify data. | Fetching a webpage or getting a user profile. |
| **POST** | Submits data to the specified resource, often resulting in a change of state. | Submitting a "Contact Us" form or creating a new user. |
| **PUT** | Replaces all current representations of the target resource with the uploaded content. | Updating a user's full profile information. |
| **DELETE** | Deletes the specified resource. | Deleting a post or removing an item from a cart. |

---

### 4. Common HTTP Status Codes

| Code | Description | Scenario |
| :--- | :--- | :--- |
| **200** | **OK** | The request succeeded (e.g., a page loaded correctly). |
| **301** | **Moved Permanently** | The URL has changed permanently. The browser redirects to the new URL. |
| **403** | **Forbidden** | The server understands the request but refuses to authorize it (e.g., accessing admin pages without admin rights). |
| **404** | **Not Found** | The server cannot find the requested resource (e.g., a broken link). |
| **500** | **Internal Server Error** | The server encountered an unexpected condition (e.g., a backend code crash). |
