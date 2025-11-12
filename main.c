#include <stdio.h>

int main(void) {
    FILE *file   = fopen("dados.txt", "r");
    FILE *output = fopen("dados_formatados.csv", "w");
    if (!file || !output) {
        printf("Erro ao abrir arquivo(s).\n");
        if (file) fclose(file);
        if (output) fclose(output);
        return 1;
    }

    int c;
    int comma_count = 0;
    int skipping = 0;

    while ((c = fgetc(file)) != EOF) {
        if (c == '\r') continue; // normaliza CRLF

        if (c == '\n') {
            fputc('\n', output);
            comma_count = 0;
            skipping = 0;
            continue;
        }

        if (skipping) {
            continue;
        }

        if (c == ',') {
            c = '.';
            fputc(c, output);
            continue;
        }

        if (c == ' ') {
            int space_count = 1;
            int next;
            while ((next = fgetc(file)) == ' ') {
                space_count++;
            }
            if (next != EOF) ungetc(next, file);

            if (space_count >= 2) {
                if (comma_count < 3) {
                    fputc(',', output);
                    comma_count++;
                } else {
                    skipping = 1;
                }
            } else {
                fputc(' ', output);
            }
            continue;
        }

        fputc(c, output);
    }

    fclose(file);
    fclose(output);
    return 0;
}

