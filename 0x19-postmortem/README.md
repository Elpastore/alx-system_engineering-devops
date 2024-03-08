# Load Balancing Failure

At the beginning of the week, after configuring our load balancer, thanks to our monitoring system, we detected an overload of our `web_01` server due to an increased number of requests. We were using two servers with a round-robin algorithm for load balancing.

## Timeline

The problem was detected on Monday, March 4th, 2024, at 10:20 AM (East Africa Time) after configuring our load balancer to handle multiple requests for our web application. Abdoulaye Sadio, our Software Engineer, detected, with the help of monitoring, that the number of requests from `web_01` was significantly higher than from `web_02` (0 requests in 2 hours). Additionally, there was a loss of customers due to a latent service.

For more than 2 hours, the problem persisted with no activity on the second `web2` server, resulting in a delayed response from our `elpastore.tech` service and causing us to lose notoriety and customers in the real estate sector. The problem was resolved at 3:00 PM (East Africa Time) on the same day.

## Root Cause and Resolution

The problem stemmed from a misconfiguration of the load balancer, even though it was configured with the round-robin balancing algorithm. The global structure of the `/etc/haproxy/haproxy.cfg` file was correct, as were the frontend and backend parts. The main error was due to an incorrect IP address for the `web_02` server when configuring the `/etc/haproxy/haproxy.cfg` file, causing requests to be redirected to the `web_01` server and overloading it.

The problem was solved by correcting the IP address of `web_02` and restarting the load balancer, which successfully balanced the loads between our two servers.

## Preventative Measures

- Always keep an eye on your servers to ensure they are running properly.
- Acquire servers with better performance to manage time overloads.
- Always ensure correct load balancer configuration.

