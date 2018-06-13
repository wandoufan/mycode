# 1xx消息:请求已被接受，需要继续处理。HTTP/1.0协议中没有定义任何1xx状态码。 
# 100 Continue 客户端应当继续发送剩余请求。 
# 101 Switching Protocols 服务器已经理解了客户端的请求，并将通过Upgrade消息头通知客户端采用不同的协议来完成这个请求。 
# 102 Processing 处理将被继续执行。

# 2xx成功:请求已成功被服务器接收、理解并接受。 
# 200 OK 请求已成功，请求所希望的响应头或数据体将随此响应返回。 
# 201 Created 请求已被实现，且有一个新的资源已经依请求的需要而创建。 
# 202 Accepted 服务器已经接受请求，但尚未处理。 
# 203 Non-Authoritative Information服务器已经成功处理了请求，但返回的实体头部元信息不是在原始服务器上有效的确定集合，而是来自本地或者第三方的拷贝。 
# 204 No Content 服务器成功处理了请求，但不需要返回任何实体内容，并且希望返回更新了的元信息。 
# 205 Reset Content 服务器成功处理了请求，且没有返回任何内容。与204相应不同，此状态码的响应要求请求者重置文档视图。 
# 206 Partial Content 服务器已成功处理了部分GET请求。可以实现断点续传。 
# 207 Multi-Status代表之后的消息体将是一个XML消息。

# 3xx重定向： 
# 300 Multiple Choices被请求的资源有一系列可供选择的回馈信息，用户自行选择一个进行重定向。 
# 301 Moved Permanently被请求的资源已永久移动到新的位置。 
# 302 Found请求的资源现在临时从不同的URI响应请求。 
# 303 See Other对应当前请求的响应可以在另一个URI上被找到而且客户端应该采用GET方式访问那个资源。 
# 304 Not Modified文档的内容没有发生改变。且304响应禁止包含消息体，因此始终以消息头后第一个空行结尾。 
# 305 Use Proxy被请求的资源必须通过指定的代理才能访问。 
# 306 Switch Proxy已弃用 
# 307 Temporary Redirect请求的资源现在临时从不同的URI响应请求。

# 4xx:客户端错误 
# 400 Bad Request请求包含语法错误。 
# 401 Unauthorized当前请求需要用户验证。 
# 402 Payment Required保留。 
# 403 Forbidden服务器已理解请求，但拒绝执行它。 
# 404 Not Found请求所需要的资源未在服务器上被发现。 
# 405 Method Not Allowed请求行中指定的方法不能用于请求相应的资源。 
# 406 Not Acceptable请求的资源的内容特性无法满足请求头中的条件，因而无法生成响应实体。 
# 407 Proxy Authentication Required与401响应类似，只不过客户端必须在代理服务器上进行身份验证。 
# 408 Request Timeout请求超时。 
# 409 Conflict由于被请求的资源的当前状态之间存在冲突，请求无法完成。 
# 410 Gone被请求的资源在服务器上已经不再可用，而且没有任何已知的转发地址。 
# 411 Length Required服务器拒绝在没有定义Content-Length头的情况下接受请求。 
# 412 Precondition Failed服务器在验证在请求的头字段中给出先决条件时，没能满足其中的一个或多个。 
# 413 Request Entity Too Large服务器拒绝处理当前请求，因为该请求提交的实体数据大小超过了服务器愿意或者能够处理的范围。 
# 414 Request-URI Too Long请求的URI长度超过了服务器能够解释的长度，因此服务器拒绝对该请求提供服务。 
# 415 Unsupported Media Type对于当前请求的方法和所请求的资源，请求中提交的实体并不是服务器中所支持的格式，因此请求被拒绝。 
# 416 Requested Range Not Satisfiable如果请求中包含了Range请求头，并且Range中指定的任何数据范围都与当前资源的可用范围不重合，同时请求中又没有定义If-Range请求头，那么服务器就应当返回416状态码。 
# 417 Expectation Failed在请求头Expect中指定的预期内容无法被服务器满足，或者这个服务器是一个代理服务器，它有明显的证据证明在当前路由的下一个节点上，Expect的内容无法被满足。 
# 418 I’m a teapot 
# 421 There are too many connections from your internet address从当前客户端所在的IP地址到服务器的连接数超过了服务器许可的最大范围。 
# 422 Unprocessable Entity请求格式正确，但是由于含有语义错误，无法响应。 
# 423 Locked当前资源被锁定。 
# 424 Failed Dependency由于之前的某个请求发生的错误，导致当前请求失败，例如PROPPATCH。 
# 425 Unordered Collection 
# 426 Upgrade Required客户端应当切换到TLS/1.0。 
# 449 Retry With由微软扩展，代表请求应当在执行完适当的操作后进行重试。 
# 451 Unavailable For Legal Reasons由IETF核准，代表该访问因法律的要求而被拒绝。

# 5xx:服务器错误 
# 500 Internal Server Error服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。 
# 501 Not Implemented服务器不支持当前请求所需要的某个功能。** 
# 502 Bad Gateway作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。 
# 503 Service Unavailable由于临时的服务器维护或者过载，服务器当前无法处理请求。 
# 504 Gateway Timeout作为网关或者代理工作的服务器尝试执行请求时，未能及时从上游服务器（URI标识出的服务器，例如HTTP、FTP、LDAP）或者辅助服务器（例如DNS）收到响应。 
# 505 HTTP Version Not Supported服务器不支持，或者拒绝支持在请求中使用的HTTP版本。 
# 506 Variant Also Negotiates代表服务器存在内部配置错误 
# 507 Insufficient Storage服务器无法存储完成请求所必须的内容。这个状况被认为是临时的。 
# 509 Bandwidth Limit Exceeded服务器达到带宽限制。这不是一个官方的状态码，但是仍被广泛使用。 
# 510 Not Extended获取资源所需要的策略并没有被满足。