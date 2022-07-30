import java.time.LocalDate;
import java.time.temporal.ChronoUnit;


public class Datas {
    private LocalDate[] data;
    private int numInsertions;
    private int size;

    public Datas(int size){
        this.numInsertions = 0;
        this.size = size;
        this.data = new LocalDate[size];
    }

    // 3. a)
    public void insereData(LocalDate data){
        if(numInsertions < size)
            this.data[this.numInsertions++] = data;

    }

    // 3. b)
    public LocalDate dataMaisProxima(LocalDate data){
        long minDist = ChronoUnit.DAYS.between(this.data[0], data);
        int i;
        int index = 0;

        for(i=0; i<this.numInsertions; i+= 1){
            long time = ChronoUnit.DAYS.between(this.data[i], data);
            if(time < minDist) {
                index = i;
                minDist = time;
            }
        }

        return this.data[index];
    }

    // 3. c)
    public String toString(){
        String string = "";
        int i;

        for(i=0; i<this.numInsertions; i+=1)
            string += this.data[i] + "\n";

        return string;
    }


}
