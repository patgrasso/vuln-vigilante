#include <stdio.h>
#include <string.h>

int lol;

void
bad_fn(char *str)
{
  char buffer[32];

  buffer[0] = '\0';

  strcat(buffer, "Hello there");
  strcat(buffer, str);

  printf(buffer);
}

int
main(int argc, char *const argv[])
{
  int i = argc + 3;
  printf("Hello there, this is the %s program.\n", argv[0]);
  printf("I got %d arguments.\n", argc);

  if (argc > 1) {
    bad_fn(argv[1]);
  }
  return 0;
}
