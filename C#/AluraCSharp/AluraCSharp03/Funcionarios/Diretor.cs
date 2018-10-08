using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp03.Funcionarios
{
    class Diretor : Funcionario
    {
        public double Aumento { get; protected set; }

        public Diretor(string nome, ulong cpf, double salario, double aumentoAnual) : base(nome, cpf, salario)
        {
            this.Aumento = aumentoAnual;
        }

        public override double GetBonificacao()
        {
            return 2 * base.GetBonificacao();
        }

        public override void AumentarSalario()
        {
            this.Salario = this.Salario * 0.2 + this.Aumento;
        }
    }
}
