There is an Apache style access log at /app/access.log. Read the log and produce a JSON summary of the traffic to /app/report.json.

The report must be a single JSON object with exactly these three keys:

- total_requests: an integer, the total number of requests in the log. Count one request per non empty line.
- unique_ips: an integer, the number of distinct client IP addresses. The client IP is the first field on each line.
- top_path: a string, the request path that appears most often. Each line has a quoted request such as "GET /index.html HTTP/1.1", and the path is the part right after the method, for example /index.html.

Do not include any additional keys in the JSON object, and save the result to /app/report.json.

Success criteria:
1. /app/report.json contains a valid JSON object with exactly the keys total_requests, unique_ips, and top_path.
2. total_requests is an integer equal to the number of requests in the log.
3. unique_ips is an integer equal to the number of distinct client IP addresses in the log.
4. top_path is a string equal to the most frequently requested path in the log.

You have 120 seconds to complete the task.
