int pesoC (GraphM g, int V[], int k){
	int i, peso = 0;

	
	for(i=0 ; i <(k-1); i++){
		if(g[v[i]][v[i+1]] == NE) return -1;
		peso += g[v[i]][v[i+1]];
	}

	return peso;
}


// Depth First

// DF - Inicialização de variáveis
int DF(Grafo g, int or){
	int i, vis[NV], pais[NV], dist[NV];
	int count;

	for(i=0; i<NV; i++){
		vis[i]=0;
		pais[i] = -2;
		dist[i] = -1;
	}
	pais[or] = -1;
	dist[or] = 0;
	count = DFRec(Grafo g, int or, vis, pais, dist);

	return count;
}


// DFRec - Parte recursiva que percorre o grafo
int DFRec(Grafo g, int or, int vis[], int pais[], int dist[]){
	LAdj aux;
	int count = 1;

	for(aux = g[or]; aux; aux=aux->prox){
	    if(!vis[aux->dest]){
	    	vis[aux->dest] = 1;
	    	pais[aux->dest] = or;
	    	dist[aux->dest] += 1;
	    	count += DFRec(g, aux->dest, vis, pais, dist);
	    }
	}


	return count;
}


int maisDist (Grafo g, int or){
	int vis[NV] = {0}, dist[NV] = {0};

	DF(g, or, vis, dist);

	max(dist)

}


// Breadth First  
int BF(Grafo g, int or){
	int vis[NV], dist[NV], pais[NV];
	int q[NV], front=0, end=0, i, count = 0;
	LAdj aux;
	
	for(i=0; i<NV; i++){
		q[i] = -1;
		vis[i] = 0;
		dist[i] = -1;
		pais[i] = -2;
	}

	//enqueue
	q[end++] = or;
	dist[or] = 0;
	pais[or] = -1;
	vis[or] = 1;

	while(front != end){
		//dequeue
		or = q[front++];
		count++;
		for(aux = g[or]; aux; aux=aux->prox){
			if(!vis[aux->dest]){
				//enqueue
				q[end++] = aux->dest;
				dist[aux->dest] = 1 + dist[or];
				pais[aux->dest] = or;
				vis[aux->dest] = 1;
			}
		}
	}


	return count;
}




