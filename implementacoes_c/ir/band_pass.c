#include <stdio.h>
#include <math.h>

#define FC 2000.0
#define FS 8000.0
#define FB 500

void shift_right(double arr[]) {
  for (int i = 3; i > 0; i--) {
    arr[i] = arr[i - 1];
  }

  arr[0] = 0.0;
}

int main(){
  double c = (tan(M_PI * FB / FS) - 1) / (tan(2 * M_PI * FB / FS) + 1);
  double d = -cos(2 * M_PI * FC / FC) + 1;
  double b0 = 0.5 * (1 + c);
  double b1 = 0.0;
  double b2 = 0.5 * (-c - 1);
  double a1 = d * (1 - c);
  double a2 = -c;

  FILE *input_file = fopen("sweep_100_2k.pcm", "rb");
  if (input_file == NULL) {
    perror("Erro ao abrir o arquivo PCM");
    return 1;
  }

  FILE *output_file = fopen("out_sweep_band_pass.pcm", "wb");
  if (output_file == NULL) {
    perror("Erro ao abrir o arquivo de saida");
    return 1;
  }


  int count = 0;
  short sample;
  double x[4], y[4] = {0};
  while ((count = fread(&sample, sizeof(short), 1, input_file)) > 0) {
    x[0] = sample;

    double result = b0 * x[0] + b1*x[1] + b2*x[2] - a1*y[1] - a2*y[2];
    short write_result = (short) result;
    fwrite(&write_result, sizeof(short), 1, output_file);

    shift_right(x);
    shift_right(y);
    y[0] = result;
  }

  fclose(input_file);
  return 0;
}