# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zsmith <zsmith@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/12/14 23:11:31 by zsmith            #+#    #+#              #
#    Updated: 2017/03/17 17:01:48 by zsmith           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME	=
FLAGS	=	-c -Wall -Wextra -Werror
CLEAKS	=	test_mallocwrap.c
CFILES	=	

LIBFILES=
			
			
SRCDIR  =	srcs/
HDIR	=	includes/
LIBDIR  =	libdir/

.PHONY: all $(NAME) clean flcean re

all: $(NAME)

$(NAME): 
	gcc $(addprefix $(SRCDIR), $(CFILES)) -o $@ -I $(HDIR)					\
		-L. $(addprefix $(LIBDIR), $(LIBFILES)) 

clean:
	/bin/rm -f $(addprefix $(SRCDIR), $(OFILES))

fclean: clean
	/bin/rm -f $(NAME)

re: fclean all



