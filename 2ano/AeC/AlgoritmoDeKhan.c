int khanTS (Grafo g, int q[]){ // q é a queue passada como parâmetro
	LAdj aux;
	int i, inicio=0, fim=0; // queue vazia
	int nAnt[NV]; // número de antecessores

	// colocar o array de antecessores todo a 0 
	for(i=0; i<NV; i++)
		nAnt[i] = 0;

	//calcular o grau de entrada -> inDegree
	for(i=0; i<N; i++)
		for(aux = g[i]; aux; aux=aux->prox)
			nAnt[aux->dest] += 1;

	// procurar os nodos que não têm nada a apontar para eles
	// ou seja, inDegree == 0
	for(i=0; i<NV; i++)
		if(nAnt[i] == 0)
			//enqueue
			q[end++] = i;

	int or;
	while(front != end){
		//dequeue
		or = q[front++];
		for(aux=g[or]; aux; aux=aux->prox){
			nAnt[aux->dest]--;
			if(!nAnt[aux->dest]){
				//enqueue
				q[end++] = aux->dest;
			}
		}
	}
	return inicio;
}