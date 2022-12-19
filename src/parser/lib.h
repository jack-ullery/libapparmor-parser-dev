#ifndef __AA_LIB_H_
#define __AA_LIB_H_

#include <sys/apparmor_private.h>

int isodigit(char c);
long strntol(const char *str, const char **endptr, int base, long maxval,
	     size_t n);
int strn_escseq(const char **pos, const char *chrs, size_t n);

#endif /* __AA_LIB_H_ */
