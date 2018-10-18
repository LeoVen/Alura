using System;
using System.Collections.Generic;
using System.Text;

namespace ByteBank.Modelos
{
    public class ClasseTeste
    {
        public int VariavelPublica = 0;
        private int VariavelPrivada = 1;
        protected int VariavelProtegida = 2;
        internal int VariavelInterna = 3;
        protected internal int VariavelProtegidaInterna = 4;
        private protected int VariavelPrivadaInterna = 5; // C# 7.2 or greater

        public void MetodoPublico()
        {
            //Visível fora da classe "ClasseTeste"
        }
        private void MetodoPrivado()
        {
            //Visível apenas na classe "ClasseTeste"
        }
        protected void MetodoProtegido()
        {
            //Visível apenas na classe "ClasseTeste" e derivados
        }
        internal void MetodoInterno()
        {
            //Visível apenas para o projeto onde a classe foi declarada
        }
        protected internal void MetodoProtegidoInterno()
        {
            //Visível apenas na classe "ClasseTeste" e derivados OU também em outras classes em outro projeto
        }
        private protected void MetodoPrivadoProtegido() // C# 7.2 or greater
        {
            //Visível apenas na classe "ClasseTeste" e derivados apenas dentro do projeto
        }
    }
}
