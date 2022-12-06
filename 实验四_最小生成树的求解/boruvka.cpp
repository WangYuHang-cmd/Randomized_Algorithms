#include<bits/stdc++.h>
#include<windows.h>
const int N = 2000010;

std::vector<int> mn[2];
std::vector<std::pair<int,int>> edge[N];

struct Boruvka{
    int n;
    std::vector<int> fa;
    Boruvka(int _n):n(_n){
        fa.resize(n+1,0);
        for(int i=0;i<=n;++i) fa[i]=i;
    }
    int find(int x){return fa[x]==x?fa[x]:fa[x]=find(fa[x]);}
    bool join(int x,int y){
        int px=find(x),py=find(y);
        if(px!=py){
            fa[px]=py;
            return true;
        }
        return false;
    }
};

void solve(){
    auto clear=[&](int n)->void{
        for(int i=0;i<=n;++i) edge[i].clear();
    };
    clear(N-1);
    //========����ͼ
    int n,m;
    // std::cout<<"������ͼ�ĵ���n�ͱ���m:\n";
    std::cin >> n >> m;
    // std::cout<<"������ͼ��ÿһ����:\n";
    for(int i=1;i<=m;++i){
        int u,v,w;
        std::cin >> u >> v >> w;
        edge[u].push_back(std::make_pair(v,w));
        edge[v].push_back(std::make_pair(u,w));
    }
    //==================================
    Boruvka T(n+1);
    mn[0].resize(n+1,0x3f3f3f3f);mn[1].resize(n+1);

    long long ans=0;//��С��������·����
    while(true){
        mn[0].resize(n+1,0x3f3f3f3f);
        bool flag=0;
        for(int i=1;i<=n;++i){
            for(auto v:edge[i]){
                int ver=v.first, w=v.second;
                if(T.find(i)!=T.find(ver))
                    if(mn[0][T.find(i)]>w)
                        mn[0][T.find(i)] = w, mn[1][T.find(i)] = T.find(ver);
            }
        }
        for(int i=1;i<=n;++i){
            if(mn[0][i]!=mn[0][0]&&T.find(i)!=T.find(mn[1][i])){
                flag=true;
                ans += mn[0][i];
                T.join(i, mn[1][i]);
            }
        }
        // std::cout<<"flag:"<<flag<<std::endl;
        if(!flag) break;
    }
    std::cout<<"��С��������·����:"<<ans<<"\n";
}

signed main(){
    freopen("in.in","r",stdin);
    clock_t st, ed;
    st = GetTickCount();
    solve(); 
    ed = GetTickCount();
    // double elapsedTime = static_cast<double>(ed-st) / CLOCKS_PER_SEC ;
    std::cout << "��ʱ:" << (ed-st) << "ms" << std::endl;
    return 0;
}

/*
����ά��ͼ��������ͨ�飬Ȼ��������еĵ�ͱߣ�
�ҵ�ÿһ����ͨ���������ͨ����������С��һ���ߣ�
Ȼ�����ͨ��ϲ��������ظ����������ֱ��ʣ��һ������ͨ�飬
�ʼ״̬��ÿ������һ����������ͨ�顣
5 10
1 2 210
2 3 22
2 4 45
1 4 23
1 5 322
1 3 23
4 3 22
4 5 3232
3 5 1
2 4 22
*/