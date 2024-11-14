#include <stdio.h>
#include <fcntl.h>

#define NSAMPLES 401	// Tamanho da média

void shift_right(short arr[]) {
    for (int i = NSAMPLES - 1; i > 0; i--) {
        arr[i] = arr[i - 1];
    }

    arr[0] = 0.0;
}

int main()
{
    FILE *in_file, *out_file;
    int i, n, n_amost;

    short entrada, saida;
    short sample[NSAMPLES] = {0x0};

    float y=0;

    float coef[NSAMPLES] = {
        #include "coef.dat"
    };

    if ((in_file = fopen("Q3_Voz_ruido.pcm","rb"))==NULL)
    {
        printf("\nErro: Nao abriu o arquivo de entrada\n");
        return 0;
    }
    if ((out_file = fopen("Sai_C_Q3_voz_ruido.pcm","wb"))==NULL)
    {
        printf("\nErro: Nao abriu o arquivo de saida\n");
        return 0;
    }

    for (i=0; i<NSAMPLES; i++){
        sample[i]=0;
    }

    do {
        y=0;

        n_amost = fread(&entrada,sizeof(short),1,in_file);
        sample[0] = entrada;

        for (n=0; n<NSAMPLES; n++){
            y += coef[n]*sample[n];
        }

        shift_right(sample);

        saida = (short) y;

        fwrite(&saida,sizeof(short),1,out_file);

    } while (n_amost);

    fclose(out_file);
    fclose(in_file);
    return 0;
}
