all: quine.c
	@gcc quine.c && ./a.out | tee tmp && diff tmp quine.c
