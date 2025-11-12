#include <stdio.h>
#include <stdlib.h>

int main(){
  system("ffmpeg --ss 0:10 -t 5 -c copy output.mp4 -i ../test.mp4");
  return 0;
}
