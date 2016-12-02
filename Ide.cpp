#include <bits/stdc++.h>
using namespace std;
 
double x[20];
double y[20];
int done[20];
 
int dis(int i,int j){
	return (x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]);
}
 
int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
    	cin>>x[i]>>y[i];
    }
    double ans=0.0;
    for(int i=0;i<n;i++){
    	if(done[i])continue;
    	int mn=1e9;
    	int idx=0;
    	for(int j=0;j<n;j++)if(i!=j and done[j]==0){
    		int door=dis(i,j);
    		if(door<mn){
    			mn=door;
    			idx=j;
    		}
    	
    	}
    	done[i]=1;
    	done[idx]=1;
    	ans=ans+sqrt(mn);
    	//cout<<ans<<'\n';
    }
    cout<<setprecision(2)<<fixed<<ans<<'\n';
    return 0;
}
