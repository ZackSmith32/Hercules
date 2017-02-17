/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   lernaean_server.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zsmith <zsmith@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/02/17 15:17:05 by zsmith            #+#    #+#             */
/*   Updated: 2017/02/17 15:19:38 by zsmith           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include "includes/ft_printf.h"

void					error(char *msg)
{
	perror(msg);
	exit(1);
}

void					response(int sockfd)
{
	int					newsockfd;
	socklen_t			clilen;
	struct sockaddr_in	cli_addr;
	char				buffer[256];
	int					n;

	clilen = sizeof(cli_addr);
	newsockfd = accept(sockfd, (struct sockaddr *)&cli_addr, &clilen);
	if (newsockfd < 0)
		error("ERROR on accept");
	ft_bzero(buffer, 256);
	n = read(newsockfd, buffer, 255);
	if (n < 0)
		error("ERROR reading from socket");
	printf("Here is the message: %s\n", buffer);
	if (!ft_strncmp(buffer, "ping", 4))
		n = write(newsockfd, "pong pong", 10);
	else
		n = write(newsockfd, "not today", 10);
	if (n < 0)
		error("ERROR writing to socket");
}

int						main(int argc, char *argv[])
{
	int					sockfd;
	int					portno;
	struct sockaddr_in	serv_addr;

	if (argc < 2)
	{
		ft_printf("ERROR, no port provided\n");
		exit(1);
	}
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if (sockfd < 0)
		error("ERROR opening socket");
	ft_bzero((char *)&serv_addr, sizeof(serv_addr));
	portno = ft_atoi(argv[1]);
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_addr.s_addr = INADDR_ANY;
	serv_addr.sin_port = htons(portno);
	if (bind(sockfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
		error("ERROR on binding");
	listen(sockfd, 5);
	response(sockfd);
	return (0);
}
