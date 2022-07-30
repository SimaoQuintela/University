import static java.lang.System.out;

public class Turma {
    private int[][] notasTurma;
    private int numAlunos;
    private int ucs;

    public Turma(int numAlunos, int ucs){
        notasTurma = new int[numAlunos][ucs];
        this.numAlunos = numAlunos;
        this.ucs = ucs;
    }

    public void setNota(int aluno, int uc, int nota){
        this.notasTurma[aluno][uc] = nota;
    }

    public int getNota(int aluno, int uc){
        return this.notasTurma[aluno][uc];
    }


    // 2. a)
    public void atualizarPauta(int aluno, int uc, int nota){
        setNota(aluno,uc,nota);
    }

    // 2. b)
    public int somaNotas(int ucIndex){
        int i, soma = 0;

        for(i=0; i<this.ucs; i+= 1) {
            soma += getNota(i, ucIndex);
        }

        return soma;
    }

    // 2. c)
    public float mediaDoAluno(int alunoIndex){
        int i, media = 0;

        for(i=0; i<this.ucs; i+=1)
            media += this.notasTurma[alunoIndex][i];

        media = media/this.ucs;

        return media;
    }

    // 2. d)
    public float mediaDaUc(int ucIndex){
        // cast para float de forma a ter divisão em ponto flutuante
        return (float)somaNotas(ucIndex)/this.ucs;
    }

    // 2. e)
    public int notaMaisAlta(){
        int i, j, max = notasTurma[0][0];

        for(i=0; i<this.numAlunos; i+=1)
            for(j=0; j<this.ucs; j+=1)
                if(notasTurma[i][j] > max)
                    max = notasTurma[i][j];

        return max;
    }

    // 2. f)
    public int notaMaisBaixa(){
        int i, j, min = notasTurma[0][0];

        for(i=0; i<this.numAlunos; i+=1)
            for(j=0; j<this.ucs; j+=1)
                if(notasTurma[i][j] < min)
                    min = notasTurma[i][j];

        return min;
    }

    // 2. g)
    public void notasAcimaDe(int valor){
        int[] result = new int[this.numAlunos*this.ucs];
        int i, j, k = 0;

        out.println("estes valores são superiores a " + valor + ": ");

        for(i=0; i<this.numAlunos; i+= 1)
            for(j=0; j<this.ucs; j+= 1)
                if(notasTurma[i][j] > valor) {
                    result[k] = notasTurma[i][j];
                    out.print(result[k]);
                    out.print("  ");
                }



    }

    // 2. h)
    public void notasDosAlunos(){
        int i, j;
        String notas = "";
        for(i=0; i<this.numAlunos; i+= 1){
            notas = notas + "Aluno " + i + ": ";
            for(j=0; j<this.ucs; j+=1){
                notas = notas + notasTurma[i][j] + " ";
            }
        }
    }

    public float mediaUcMaisAlta(){
        float max = 0;
        int indice = 0;
        int i;
        float media;

        for(i=0; i<this.ucs; i+=1){
            media = mediaDaUc(i);
            if(media > max){
                max = media;
                indice = i;
            }
        }

        return indice;
    }



}
