import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class FBFeed {
    private List<FBPost> posts;

    public FBFeed(){
        this.posts = new ArrayList<FBPost>();
    }

    public FBFeed(List<FBPost> posts){
        this.posts = new ArrayList<FBPost>();
        for(FBPost p: posts){
            this.posts.add(p.clone());
        }
    }

    public FBFeed(FBFeed f){
        this(f.posts);
    }

    public boolean equals(Object o){
        if(o == this)
            return true;

        if(o == null || o.getClass() != this.getClass())
            return false;

        FBFeed f = (FBFeed) o;
        /* caso dê falso nem entra no ciclo */
        boolean  r = this.posts.size() == f.posts.size();
        for(int i=0; i<this.posts.size() && r; i+=1){
            r = this.posts.get(i).equals(f.posts.get(i));
        }

        return r;
    }

    public FBFeed clone(){
        return new FBFeed(this);
    }

    // 4 b. i.
    public int nrPosts(String user){
        return (int)this.posts.stream()
                              .filter(p -> p.getUser().equals(user))
                              .count();
    }

    // 4 b. ii.
    public List<FBPost> postsOf(String user){
        List<FBPost> userPosts = new ArrayList<FBPost>();
        for(FBPost p: this.posts){
            if(p.getUser().equals(user))
                userPosts.add(p.clone());
        }

        return userPosts;
    }

    /* resolução alternativa e mais compacta
    public List<FBPost> postsOf(String user){
        return this.posts.stream().filter(a->a.getUser().equals(user)).collect(Collectors.toList());
    }
     */
    // 4 b. iii.
    public List<FBPost> postsOf(String user, LocalDateTime inicio, LocalDateTime fim){
        return this.posts.stream()
                         .filter(a -> a.getUser().equals(user) && (a.getUploadTime()).isAfter(inicio) && (a.getUploadTime()).isBefore(fim))
                         .collect(Collectors.toList());
    }

    // 4 b. iv.
    public FBPost getPost(int id){
        FBPost p = null;
        boolean founded = false;
        for(int i=0; i<this.posts.size() && !founded; i+=1){
            if(this.posts.get(i).getId() == id) {
                p = this.posts.get(i).clone();
                founded = true;
            }
        }

        return p;
    }
    /* forma alternativa, até é mais adequada neste caso
    public FBPost getPost(int id){
        FBPost r = this.post.stream().filter(a->a.getId == id).findFirst().orElse(null);
        if(r!=null)
            r = r.clone();
        return r;
    }
     */
    // 4 b. v.
    public void comment(FBPost post, String comentario){
        post.adicionaComment(comentario);
        boolean found = false;
        int i;
        for(i=0; i<this.posts.size() && !found; i+=1){
            FBPost p = this.posts.get(i);
            if(p.equals(post)){
                found = true;
            }
        }

        // se não encontro o post adiciono na última posição
        if(!found)
            this.posts.add(post.clone());
        else {
            i -= 1;
            this.posts.set(i, post.clone());
        }
    }

    // 4 b. vi. duvidoso
    public void comment(int postid, String comentario){
        boolean found = false;
        int i;
        for(i=0; i<this.posts.size() && !found; i+=1){
            FBPost p = this.posts.get(i);
            if(p.getId() == postid){
                found = true;
                p.adicionaComment(comentario);
                this.posts.set(i, p);
            }
        }
    }

    //4 b. vii.
    public void like(FBPost post){
        int i;
        boolean found = false;

        for(i=0; i<this.posts.size() && !found; i+=1){
            FBPost p = this.posts.get(i);
            if(p.equals(post)){
                found = true;
                p.setLikes(p.getLikes() +1);
                this.posts.set(i, p);
            }
        }
    }

    //4 b. viii.
    public void like(int postid){
        int i;
        boolean found=false;

        for(i=0; i<this.posts.size() && !found; i+=1){
            FBPost p = this.posts.get(i);
            if(p.getId() == postid){
                found = true;
                p.setLikes(p.getLikes()+1);
                this.posts.set(i,p);
            }
        }
    }

    //4 b. ix. retirado de https://github.com/Carricossauro/Programacao-Orientada-a-Objetos/blob/main/Ficha%204/src/exercicios/FBFeed.java
    public List<Integer> top5Comments(){
        ArrayList<FBPost> lista = new ArrayList<>(this.posts);

        lista.sort(Comparator.comparing(FBPost::getId));
        Collections.reverse(lista);

        return lista.stream().mapToInt(FBPost::getId).limit(5).boxed().collect(Collectors.toList());
    }


}

