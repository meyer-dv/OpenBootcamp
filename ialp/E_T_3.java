public class E_T_3 {
    public static void main(String[] args) {
        // Primera parte
        System.out.println(suma(1,2,3));
        
        // Segunda parte
        Coche miCoche = new Coche();
        miCoche.mPuertas();
        System.out.println(miCoche.nPuertas);
    }
    
    public static int suma(int a, int b, int c){
        return a + b + c;
    }
}

class Coche {
        public int nPuertas;
        
        public void mPuertas (){
            this.nPuertas++;
        }
    }
