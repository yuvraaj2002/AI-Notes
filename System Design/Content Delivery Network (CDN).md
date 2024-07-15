This page is dedicated towards understanding the concept of CDN in system design and the resources used for this topic are mentioned below 


- [How CDN works by CloudFare](https://www.cloudflare.com/en-in/learning/cdn/what-is-a-cdn/)
- [How Giphy uses CDN to serve 10 billion GIFs every day](https://www.youtube.com/watch?v=-bo7oVejgRM)
- [Giphy official blog about](https://engineering.giphy.com/how-giphy-uses-fastly-to-achieve-global-scale/)

#### What is CDN and what is the need of this ? 

CDN stands for content delivery network and it is network of strategically distributed servers across geographical locations to serve the static content to the user with lowest latency possible. The static content could be like images, videos, JavaScript files and API responses as well.

```
{
  "articles": [
    {
      "title": "Tech Giant Launches New AI Research Initiative",
      "source": "TechNews",
      "published_at": "2024-07-10T08:00:00Z"
    },
    {
      "title": "Global Market Insights for Q3 2024",
      "source": "FinanceToday",
      "published_at": "2024-07-10T09:30:00Z"
    }
  ]
}
```

![[Pasted image 20240710081132.png]]

A properly configured CDN may also help protect websites against some common malicious attacks, such as [Distributed Denial of Service (DDOS) attacks](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/). The typical flow is that

1. User makes request
2. The request goes to CDN and if its present in the cache then its give the response back
3. Incase the request is not stored in the cache then CDN communicates with the origin server and then cache that response for future use.


#### Need of multi layer caching ? 

😲Typically in a single regions hundreds or thousands of CDN servers could be present with ***independent cache*** and incase there is Cache miss then all those CDN servers will make a request to the origin server, so to handle such kind of load the CDN also use multi layer caching mechanism. 

In the multi level caching mechanism, rather than simply connecting the CDN servers with the origin server we introduce Origin shield servers which have their own cache and in this way the load on the Origin server is reduced in cache of cache miss from multiple CDN servers.

![[Pasted image 20240710075220.png]]




