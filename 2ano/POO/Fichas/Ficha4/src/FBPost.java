import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class FBPost {
    private int id;
    private String user;
    private LocalDateTime uploadTime;
    private String content;
    private int likes;
    private List<String> comments;

    public FBPost(){
        this.id = 0;
        this.user = "";
        this.uploadTime = LocalDateTime.now();
        this.content = "";
        this.likes = 0;
        this.comments = new ArrayList<String>();
    }

    public FBPost(int id, String user, LocalDateTime uploadTime, String content, int likes, List<String> comments){
        this.id = id;
        this.user = user;
        this.uploadTime = uploadTime;
        this.content = content;
        this.likes = likes;
        this.comments = new ArrayList<String>(comments);
    }

    public FBPost(FBPost p){
        this(p.id, p.user, p.uploadTime, p.content, p.likes, p.comments);
    }

    public FBPost clone(){
        return new FBPost(this);
    }

    public boolean equals(Object o){
        if(this == o)
            return true;

        if(o == null || o.getClass() != this.getClass())
            return false;

        FBPost p = (FBPost) o;

        return(
              this.id == p.id && this.user.equals(p.user) &&
              this.uploadTime.equals(p.uploadTime) && this.content.equals(p.content) &&
              this.likes == p.likes && this.comments.equals(p.comments)
            );
    }

    public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append("Id: " ).append(this.id);
        sb.append("\nUser: ").append(this.user);
        sb.append("\nData do post: ").append(this.uploadTime);
        sb.append("\nConteúdo: ").append(this.content);
        sb.append("\nLikes: ").append(this.likes);

        return sb.toString();
    }

    // adiciona um comentário ao post
    public void adicionaComment(String comment){
        this.comments.add(comment);
    }

    //gets e sets
    public int getId() {
        return this.id;
    }

    public String getUser() {
        return this.user;
    }

    public LocalDateTime getUploadTime() {
        return this.uploadTime;
    }

    public String getContent() {
        return this.content;
    }

    public int getLikes() {
        return this.likes;
    }
    /* será esta forma mais adequada do que a de baixo?
    public ArrayList<String> getComments() {
        ArrayList<String> novo = new ArrayList<String>();
        for(String c : this.comments){
            novo.add(c);
        }
        return novo;
    }
    */
    public ArrayList<String> getComments() {
        return new ArrayList<String>(this.comments);
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setUser(String user) {
        this.user = user;
    }

    public void setUploadTime(LocalDateTime uploadTime) {
        this.uploadTime = uploadTime;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public void setLikes(int likes) {
        this.likes = likes;
    }

    public void setComments(ArrayList<String> comments) {
        this.comments = new ArrayList<String>(comments);
    }
}
