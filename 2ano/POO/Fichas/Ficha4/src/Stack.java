import java.util.ArrayList;

public class Stack {
    private ArrayList<String> stack;

    public Stack(){
        this.stack =  new ArrayList<String>();
    }

    public Stack(ArrayList<String> s){
        this.stack = new ArrayList<String>(s);
    }

    public Stack(Stack s){
        this(s.stack);
    }

    public boolean equals(Object o){
        if(this == o)
            return true;
        if( (null == o) || (this.getClass() != o.getClass()))
            return false;

        Stack s = (Stack)o;
        return this.stack.equals(s.stack);
    }

    public String toString(){
        return this.stack.toString();
    }

    public Stack clone(){
        return new Stack(this);
    }

    //1 a.
    public String top(){
        return this.stack.get(this.stack.size() -1);
    }

    //1 b.
    public void push(String s){
        // por default acrescenta no fim
        this.stack.add(s);
    }

    //1 c.
    public void pop(){
        this.stack.remove(this.stack.size() -1);
    }

    //1 d.
    public boolean empty(){
        return this.stack.isEmpty();
    }

    //1 e.
    public int length(){
        return this.stack.size();
    }

}
