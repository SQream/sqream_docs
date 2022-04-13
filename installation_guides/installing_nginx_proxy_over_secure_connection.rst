.. _installing_nginx_proxy_over_secure_connection:

*************************
Installing an NGINX Proxy Over a Secure Connection
*************************
Configuring your NGINX server to use a strong encryption for client connections provides you with secure servers requests, preventing outside parties from gaining access to your traffic.

The **Installing an NGINX Proxy Over a Secure Connection** page describes the following:

.. contents::
   :local:
   :depth: 1

Overview
==============
The Node.js platform that SQream uses with our Studio user interface is susceptible to web exposure. This page describes how to implement HTTPS access on your proxy server to establish a secure connection.

**TLS (Transport Layer Security)**, and its predecessor **SSL (Secure Sockets Layer)**, are standard web protocols used for wrapping normal traffic in a protected, encrypted wrapper. This technology prevents the interception of server-client traffic. It also uses a certificate system for helping users verify the identity of sites they visit. The **Installing an NGINX Proxy Over a Secure Connection** guide describes how to set up a self-signed SSL certificate for use with an NGINX web server on a CentOS 7 server.

.. note:: A self-signed certificate encrypts communication between your server and any clients. However, because it is not signed by trusted certificate authorities included with web browsers, you cannot use the certificate to automatically validate the identity of your server.

A self-signed certificate may be appropriate if your domain name is not associated with your server, and in cases where your encrypted web interface is not user-facing. If you do have a domain name, using a CA-signed certificate is generally preferrable.

For more information on setting up a free trusted certificate, see `How To Secure Nginx with Let's Encrypt on CentOS 7 <https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-centos-7>`_.

Prerequisites
==============
The following prerequisites are required for installing an NGINX proxy over a secure connection:

* Super user privileges

   ::
   
* A domain name to create a certificate for

Installing NGINX and Adjusting the Firewall
==============
After verifying that you have the above preriquisites, you must verify that the NGINX web server has been installed on your machine.

Though NGINX is not available in the default CentOS repositories, it is available from the **EPEL (Extra Packages for Enterprise Linux)** repository.

**To install NGINX and adjust the firewall:**

1. Enable the EPEL repository to enable server access to the NGINX package:

   .. code-block:: console

      $ sudo yum install epel-release

2. Install NGINX:

   .. code-block:: console

      $ sudo yum install nginx
 
3. Start the NGINX service:

   .. code-block:: console

      $ sudo systemctl start nginx
 
4. Verify that the service is running:

   .. code-block:: console

      $ systemctl status nginx

   The following is an example of the correct output:

   .. code-block:: console

      Output● nginx.service - The nginx HTTP and reverse proxy server
         Loaded: loaded (/usr/lib/systemd/system/nginx.service; disabled; vendor preset: disabled)
         Active: active (running) since Fri 2017-01-06 17:27:50 UTC; 28s ago

      . . .

      Jan 06 17:27:50 centos-512mb-nyc3-01 systemd[1]: Started The nginx HTTP and reverse proxy server.

5. Enable NGINX to start when your server boots up:

   .. code-block:: console

      $ sudo systemctl enable nginx
 
6. Verify that access to **ports 80 and 443** are not blocked by a firewall.

    ::
	
7. Do one of the following:

   * If you are not using a firewall, skip to :ref:`Creating Your SSL Certificate<creating_your_ssl_certificate>`.

      ::
	  
   * If you have a running firewall, open ports 80 and 443:

     .. code-block:: console

        $ sudo firewall-cmd --add-service=http
        $ sudo firewall-cmd --add-service=https
        $ sudo firewall-cmd --runtime-to-permanent 

8. If you have a running **iptables firewall**, for a basic rule set, add HTTP and HTTPS access:

   .. code-block:: console

      $ sudo iptables -I INPUT -p tcp -m tcp --dport 80 -j ACCEPT
      $ sudo iptables -I INPUT -p tcp -m tcp --dport 443 -j ACCEPT

   .. note:: The commands in Step 8 above are highly dependent on your current rule set.

9. Verify that you can access the default NGINX page from a web browser.

.. _creating_your_ssl_certificate:

Creating Your SSL Certificate
==============
After installing NGINX and adjusting your firewall, you must create your SSL certificate.

TLS/SSL combines public certificates with private keys. The SSL key, kept private on your server, is used to encrypt content sent to clients, while the SSL certificate is publicly shared with anyone requesting content. In addition, the SSL certificate can be used to decrypt the content signed by the associated SSL key. Your public certificate is located in the **/etc/ssl/certs** directory on your server.

This section describes how to create your **/etc/ssl/private directory**, used for storing your private key file. Because the privacy of this key is essential for security, the permissions must be locked down to prevent unauthorized access:

**To create your SSL certificate:**

1. Set the following permissions to **private**:

   .. code-block:: console

      $ sudo mkdir /etc/ssl/private
      $ sudo chmod 700 /etc/ssl/private
 
2. Create a self-signed key and certificate pair with OpenSSL with the following command:

   .. code-block:: console

      $ sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt
 
   The following list describes the elements in the command above:
   
   * **openssl** - The basic command line tool used for creating and managing OpenSSL certificates, keys, and other files.
   
    ::

   * **req** - A subcommand for using the X.509 **Certificate Signing Request (CSR)** management. A public key infrastructure standard, SSL and TLS adhere X.509 key and certificate management regulations.

    ::

   * **-x509** - Used for modifying the previous subcommand by overriding the default functionality of generating a certificate signing request with making a self-signed certificate.

    ::

   * **-nodes** - Sets **OpenSSL** to skip the option of securing our certificate with a passphrase, letting NGINX read the file without user intervention when the server is activated. If you don't use **-nodes** you must enter your passphrase after every restart.

    ::

   * **-days 365** - Sets the certificate's validation duration to one year.

    ::

   * **-newkey rsa:2048** - Simultaneously generates a new certificate and new key. Because the key required to sign the certificate was not created in the previous step, it must be created along with the certificate. The **rsa:2048** generates an RSA 2048 bits long.

    ::

   * **-keyout** - Determines the location of the generated private key file.

    ::

   * **-out** - Determines the location of the certificate.

  After creating a self-signed key and certificate pair with OpenSSL, a series of prompts about your server is presented to correctly embed the information you provided in the certificate.

3. Provide the information requested by the prompts.

   The most important piece of information is the **Common Name**, which is either the server **FQDN** or **your** name. You must enter the domain name associated with your server or your server’s public IP address.

   The following is an example of a filled out set of prompts:

   .. code-block:: console

      OutputCountry Name (2 letter code) [AU]:US
      State or Province Name (full name) [Some-State]:New York
      Locality Name (eg, city) []:New York City
      Organization Name (eg, company) [Internet Widgits Pty Ltd]:Bouncy Castles, Inc.
      Organizational Unit Name (eg, section) []:Ministry of Water Slides
      Common Name (e.g. server FQDN or YOUR name) []:server_IP_address
      Email Address []:admin@your_domain.com

   Both files you create are stored in their own subdirectories of the **/etc/ssl** directory.

   Although SQream uses OpenSSL, in addition we recommend creating a strong **Diffie-Hellman** group, used for negotiating **Perfect Forward Secrecy** with clients.
   
4. Create a strong Diffie-Hellman group:

   .. code-block:: console

      $ sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
 
   Creating a Diffie-Hellman group takes a few minutes, which is stored as the **dhparam.pem** file in the **/etc/ssl/certs** directory. This file can use in the configuration.
   
Configuring NGINX to use SSL
==============
After creating your SSL certificate, you must configure NGINX to use SSL.

The default CentOS NGINX configuration is fairly unstructured, with the default HTTP server block located in the main configuration file. NGINX checks for files ending in **.conf** in the **/etc/nginx/conf.d** directory for additional configuration.

SQream creates a new file in the **/etc/nginx/conf.d** directory to configure a server block. This block serves content using the certificate files we generated. In addition, the default server block can be optionally configured to redirect HTTP requests to HTTPS.

.. note:: The example on this page uses the IP address **127.0.0.1**, which you should replace with your machine's IP address.

**To configure NGINX to use SSL:**

1. Create and open a file called **ssl.conf** in the **/etc/nginx/conf.d** directory:

   .. code-block:: console

      $ sudo vi /etc/nginx/conf.d/ssl.conf

2. In the file you created in Step 1 above, open a server block:

   1. Listen to **port 443**, which is the TLS/SSL default port.
   
       ::
   
   2. Set the ``server_name`` to the server’s domain name or IP address you used as the Common Name when generating your certificate.
   
       ::
	   
   3. Use the ``ssl_certificate``, ``ssl_certificate_key``, and ``ssl_dhparam`` directives to set the location of the SSL files you generated, as shown in the **/etc/nginx/conf.d/ssl.conf** file below:
   
   .. code-block:: console

          upstream ui {
              server 127.0.0.1:8080;
          }
      server {
          listen 443 http2 ssl;
          listen [::]:443 http2 ssl;

          server_name nginx.sq.l;

          ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;
          ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;
          ssl_dhparam /etc/ssl/certs/dhparam.pem;

      root /usr/share/nginx/html;

      #    location / {
      #    }

        location / {
              proxy_pass http://ui;
              proxy_set_header           X-Forwarded-Proto https;
              proxy_set_header           X-Forwarded-For $proxy_add_x_forwarded_for;
              proxy_set_header           X-Real-IP       $remote_addr;
              proxy_set_header           Host $host;
                      add_header                 Front-End-Https   on;
              add_header                 X-Cache-Status $upstream_cache_status;
              proxy_cache                off;
              proxy_cache_revalidate     off;
              proxy_cache_min_uses       1;
              proxy_cache_valid          200 302 1h;
              proxy_cache_valid          404 3s;
              proxy_cache_use_stale      error timeout invalid_header updating http_500 http_502 http_503 http_504;
              proxy_no_cache             $cookie_nocache $arg_nocache $arg_comment $http_pragma $http_authorization;
              proxy_redirect             default;
              proxy_max_temp_file_size   0;
              proxy_connect_timeout      90;
              proxy_send_timeout         90;
              proxy_read_timeout         90;
              proxy_buffer_size          4k;
              proxy_buffering            on;
              proxy_buffers              4 32k;
              proxy_busy_buffers_size    64k;
              proxy_temp_file_write_size 64k;
              proxy_intercept_errors     on;

              proxy_set_header           Upgrade $http_upgrade;
              proxy_set_header           Connection "upgrade";
          }

          error_page 404 /404.html;
          location = /404.html {
          }

          error_page 500 502 503 504 /50x.html;
          location = /50x.html {
          }
      }
 
4. Open and modify the **nginx.conf** file located in the **/etc/nginx/conf.d** directory as follows:

   .. code-block:: console

      $ sudo vi /etc/nginx/conf.d/nginx.conf
	 
   .. code-block:: console      

       server {
           listen       80;
           listen       [::]:80;
           server_name  _;
           root         /usr/share/nginx/html;

           # Load configuration files for the default server block.
           include /etc/nginx/default.d/*.conf;

           error_page 404 /404.html;
           location = /404.html {
           }

           error_page 500 502 503 504 /50x.html;
           location = /50x.html {
           }
       }
	   
Redirecting Studio Access from HTTP to HTTPS
==================
After configuring NGINX to use SSL, you must redirect Studio access from HTTP to HTTPS.

According to your current configuration, NGINX responds with encrypted content for requests on port 443, but with **unencrypted** content for requests on **port 80**. This means that our site offers encryption, but does not enforce its usage. This may be fine for some use cases, but it is usually better to require encryption. This is especially important when confidential data like passwords may be transferred between the browser and the server.

The default NGINX configuration file allows us to easily add directives to the default port 80 server block by adding files in the /etc/nginx/default.d directory.

**To create a redirect from HTTP to HTTPS:**

1. Create a new file called **ssl-redirect.conf** and open it for editing:

   .. code-block:: console

      $ sudo vi /etc/nginx/default.d/ssl-redirect.conf

2. Copy and paste this line:

   .. code-block:: console

      $ return 301 https://$host$request_uri:8080/;
	  
Activating Your NGINX Configuration
==============
After redirecting from HTTP to HTTPs, you must restart NGINX to activate your new configuration.

**To activate your NGINX configuration:**

1. Verify that your files contain no syntax errors:

   .. code-block:: console

      $ sudo nginx -t
   
   The following output is generated if your files contain no syntax errors:

   .. code-block:: console

      nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
      nginx: configuration file /etc/nginx/nginx.conf test is successful

2. Restart NGINX to activate your configuration:

   .. code-block:: console

      $ sudo systemctl restart nginx

Verifying that NGINX is Running
==============
After activating your NGINX configuration, you must verify that NGINX is running correctly.

**To verify that NGINX is running correctly:**

1. Check that the service is up and running:

   .. code-block:: console

      $ systemctl status nginx
  
   The following is an example of the correct output:

   .. code-block:: console

      Output● nginx.service - The nginx HTTP and reverse proxy server
         Loaded: loaded (/usr/lib/systemd/system/nginx.service; disabled; vendor preset: disabled)
         Active: active (running) since Fri 2017-01-06 17:27:50 UTC; 28s ago

      . . .

      Jan 06 17:27:50 centos-512mb-nyc3-01 systemd[1]: Started The nginx HTTP and reverse proxy server.
 
2. Run the following command:

   .. code-block:: console

      $ sudo netstat -nltp |grep nginx
 
   The following is an example of the correct output:

   .. code-block:: console

      [sqream@dorb-pc etc]$ sudo netstat -nltp |grep nginx
      tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      15486/nginx: master 
      tcp        0      0 0.0.0.0:443             0.0.0.0:*               LISTEN      15486/nginx: master 
      tcp6       0      0 :::80                   :::*                    LISTEN      15486/nginx: master 
      tcp6       0      0 :::443                  :::*                    LISTEN      15486/nginx: master