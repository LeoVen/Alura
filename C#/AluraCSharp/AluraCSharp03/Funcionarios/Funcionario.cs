using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp03.Funcionarios
{
    class Funcionario
    {
        public static ulong TotalFuncionarios { get; private set; } = 0;

        public string Nome { get; protected set; }
        public ulong CPF { get; protected set; }
        public double Salario { get; protected set; }

        public Funcionario(string nome, ulong cpf, double salario)
        {
            this.Nome = nome;
            this.CPF = cpf;
            this.Salario = salario;

            TotalFuncionarios++;
        }

        public virtual double GetBonificacao()
        {
            return this.Salario * 0.1;
        }

        public virtual void AumentarSalario()
        {
            this.Salario *= 0.1;
        }
    }
}
