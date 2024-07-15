This page is actually dedicated towards understanding the concept to of DNS in computer networks or system design and the resources used for this topic are mentioned below.

- [Technical Guftgu](https://www.youtube.com/watch?v=1aEL4kZJbvs)
- [What is DNS? | How DNS works](https://www.cloudflare.com/en-in/learning/dns/what-is-dns/)
- [Arpit Bhayani](https://www.youtube.com/watch?v=g_gKI2HCElk)


#### What is DNS and what is the use of it ? 

DNS stands for domain name system and in very simple terms it can be described as the phonebook of the internet which store the IP address of every domain. So whenever we type something on our web browser like www.abc.com then the DNS translate this domain to its corresponding IP address as machines communicate with each other via logical addresses (IP addresses only).

With the help of DNS the users don't have to remember complex IP address of every webpage. Also an important thing that we must keep in mind is that the DNS is not only responsible for 1 way translation instead it can also map the IP address to its corresponding Domain name as well.

![[Pasted image 20240710061701.png|550]]


#### DNS servers involved in loading a webpage

**In order to load a webpage, there are 4 types of DNS servers that work under the hood. Here's an explanation of each server:**

1. **Recursive DNS Resolver**: This server acts as an intermediary between the client and the DNS infrastructure. It runs a program on a server at the application layer and handles the entire DNS lookup process on behalf of the client. It makes recursive requests to the DNS hierarchy until the domain is resolved. Often, frequently visited domains are stored in the resolver's cache, so the IP address can be retrieved quickly without querying other servers.

2. **Root Name Server**: The root name server is at the top level of the DNS hierarchy. It does not map domain names to IP addresses. Instead, it directs the DNS query to the appropriate top-level domain (TLD) server based on the domain extension (like .com, .org, .edu). Currently, there are 13 sets of root name servers distributed worldwide.

3. **Top-Level Domain (TLD) Name Server**: After the root name server, the TLD name server handles DNS queries for specific domain extensions. When it receives a query from the root name server, it directs the query to the appropriate authoritative name server for that domain.

4. **Authoritative Name Server**: This is the final step in the DNS hierarchy. The authoritative name server holds the actual DNS records and provides the IP address corresponding to the requested domain name.

![[Pasted image 20240710065249.png]]
