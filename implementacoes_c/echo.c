#include <stdio.h>
#include <fcntl.h>

#define NSAMPLES 32	// Tamanho da média
#define D 4

int main()
{
    FILE *in_file, *out_file;
    int i, n, n_amost;

    short entrada, saida;
    short sample[NSAMPLES] = {0x0};

    float y=0;

    //Carregando os coeficientes do filtro média móvel
    float coef[NSAMPLES]={
        #include "coefs_echo.dat"
    };

   /* abre os arquivos de entrada e saida */
    if ((in_file = fopen("sweep_100_2k.pcm","rb"))==NULL)
    {
        printf("\nErro: Nao abriu o arquivo de entrada\n");
        return 0;
    }
    if ((out_file = fopen("sai_sweep_mm_16.pcm","wb"))==NULL)
    {
        printf("\nErro: Nao abriu o arquivo de saida\n");
        return 0;
    }

    // zera vetor de amostras
    for (i=0; i<NSAMPLES; i++)
    {
        sample[i]=0;
    }

    // execução do filtro
    do {
        
        //zera saída do filtro
        y=0;

        //lê dado do arquivo
        n_amost = fread(&entrada,sizeof(short),1,in_file);
        sample[0] = entrada;

        //Convolução e acumulação
        for (n=0; n<NSAMPLES; n++)
        {
            y += coef[0]*sample[n] + coef[1]*;
        }

        //desloca amostra
        for (n=NSAMPLES-1; n>0; n--)
        {
            sample[n]=sample[n-1];
        }

        saida = (short) y;

        //escreve no arquivo de saída
        fwrite(&saida,sizeof(short),1,out_file);

    } while (n_amost);


    //fecha os arquivos de entrada de saída
    fclose(out_file);
    fclose(in_file);
    return 0;
}
