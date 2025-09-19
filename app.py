import streamlit as st

html_code = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora Financeira</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-color: #2E86DE;
            --secondary-color: #A3A3A3;
            --accent-color: #F1C40F;
            --success-color: #27AE60;
            --danger-color: #E74C3C;
            --bg-dark: #2C3E50;
            --bg-light: #F4F6F9;
            --text-dark: #34495E;
            --text-light: #ECF0F1;
            --card-bg: #FFFFFF;
        }

        body {
            font-family: 'Roboto', sans-serif;
            background-color: var(--bg-light);
            color: var(--text-dark);
            margin: 0;
            padding: 1rem;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            min-height: 100vh;
        }

        .container {
            background-color: var(--card-bg);
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            max-width: 900px;
            width: 100%;
        }

        h1, h3, h4 {
            color: var(--primary-color);
            text-align: center;
        }
        
        h1 {
            margin-bottom: 0.5rem;
        }
        
        p.subtitle {
            text-align: center;
            color: var(--secondary-color);
            margin-bottom: 2rem;
        }

        .tab-buttons {
            display: flex;
            justify-content: center;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }
        
        .tab-btn {
            background-color: #EFEFEF;
            border: none;
            padding: 12px 18px;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            margin: 5px;
            border-radius: 8px;
        }
        
        .tab-btn:hover {
            background-color: #DEDEDE;
        }
        
        .tab-btn.active {
            background-color: var(--primary-color);
            color: var(--text-light);
            font-weight: 500;
        }
        
        .tab-content {
            display: none;
        }
        
        .tab-content.active {
            display: block;
        }
        
        .form-group {
            margin-bottom: 1.5rem;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: bold;
            color: var(--text-dark);
        }
        
        .form-group input {
            width: calc(100% - 22px);
            padding: 11px;
            border: 1px solid #ced4da;
            border-radius: 8px;
            font-size: 1rem;
            transition: border-color 0.3s ease, box-shadow 0.3s ease;
        }
        
        .form-group input:focus {
            outline: none;
            border-color: var(--primary-color);
            box-shadow: 0 0 5px rgba(46, 134, 222, 0.5);
        }
        
        .button-group {
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            margin-top: 2rem;
            flex-wrap: wrap;
        }
        
        .btn {
            padding: 12px 24px;
            font-size: 1rem;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            flex-grow: 1;
            min-width: 150px;
        }
        
        .btn-primary {
            background-color: var(--primary-color);
            color: var(--text-light);
        }
        
        .btn-primary:hover {
            background-color: #21618C;
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        
        .btn-secondary {
            background-color: var(--secondary-color);
            color: var(--text-light);
        }
        
        .btn-secondary:hover {
            background-color: #7B7B7B;
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        
        .summary, .cdi-card, .comparison-card, .explanation {
            background-color: #F8F9FA;
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 1.5rem;
            text-align: center;
        }

        .summary p {
            font-size: 1.5rem;
            font-weight: 700;
            margin: 0.5rem 0;
            color: var(--text-dark);
        }

        .summary p.total-juros {
            color: var(--primary-color);
        }

        .summary p.final-balance {
            color: var(--success-color);
        }
        
        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            margin-top: 1rem;
            overflow: hidden;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        }
        
        table th, table td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #EAEAEA;
        }
        
        table th {
            background-color: var(--primary-color);
            color: var(--text-light);
            font-weight: 500;
            font-size: 0.9rem;
        }
        
        table tbody tr:nth-child(even) {
            background-color: #F8F9FA;
        }
        
        .explanation h3 {
            color: var(--primary-color);
        }
        
        .explanation p {
            line-height: 1.6;
        }
        
        .cdi-card {
            background-color: #EAF2F8;
            border: 1px solid #B0C4DE;
            text-align: center;
        }
        
        .cdi-card h4 {
            color: var(--primary-color);
        }
        
        .cdi-card a {
            color: var(--primary-color);
            text-decoration: none;
            font-weight: bold;
        }
        
        .comparison-card {
            background-color: #E8F6F3;
            border: 1px solid #52BE80;
        }
        
        .comparison-card h4 {
            color: var(--success-color);
        }
        
        .comparison-card .winner {
            font-size: 1.6rem;
            font-weight: 700;
            color: var(--success-color);
        }
        
        .chart-container {
            margin-top: 2rem;
        }

        @media (max-width: 768px) {
            .container {
                padding: 1rem;
                margin: 0.5rem;
            }
            h1 {
                font-size: 1.5rem;
            }
            .tab-btn {
                font-size: 0.9rem;
                padding: 10px 15px;
            }
            .btn {
                width: 100%;
            }
            .button-group {
                flex-direction: column;
            }
            table, .summary {
                font-size: 0.9rem;
            }
        }
        
    </style>
</head>
<body>

    <div class="container">
        <h1>Calculadora Financeira</h1>
        <p class="subtitle">Análise de Juros, Saques e Custo de Oportunidade</p>

        <div class="tab-buttons">
            <button class="tab-btn active" onclick="showTab('tab-saques')">Juros com Saques</button>
            <button class="tab-btn" onclick="showTab('tab-oportunidade')">Custo de Oportunidade</button>
            <button class="tab-btn" onclick="showTab('tab-explanation')">Explicação</button>
        </div>

        <div id="tab-saques" class="tab-content active">
            <div class="cdi-card">
                <h4>Taxa de Juros de Referência (CDI)</h4>
                <p>Para obter o valor atual do CDI, consulte a taxa SELIC no site oficial do Banco Central. O CDI geralmente acompanha a SELIC de perto.</p>
                <a href="https://www.bcb.gov.br/" target="_blank">Consultar no site do Banco Central</a>
            </div>
            
            <form id="saques-form">
                <div class="form-group">
                    <label for="initial-principal-saques">Capital Inicial (R$)</label>
                    <input type="number" id="initial-principal-saques" value="3000" step="0.01" required>
                </div>
                <div class="form-group">
                    <label for="monthly-withdrawal-saques">Retirada Mensal (R$)</label>
                    <input type="number" id="monthly-withdrawal-saques" value="300" step="0.01" required>
                </div>
                
                <div class="form-group">
                    <div class="flex-row">
                        <label for="monthly-rate-saques">Taxa Mensal (%)</label>
                        <input type="checkbox" id="use-cdi-saques" onclick="toggleCdiRate('saques')">
                        <label for="use-cdi-saques" style="font-weight: normal; margin-left: 5px;">Usar 100% do CDI</label>
                    </div>
                    <input type="number" id="monthly-rate-saques" value="1" step="0.01" required>
                </div>
                
                <div class="form-group" id="cdi-rate-group-saques" style="display: none;">
                    <label for="cdi-annual-rate-saques">Taxa Anual do CDI (%)</label>
                    <input type="number" id="cdi-annual-rate-saques" value="10" step="0.01" required>
                </div>
                
                <div class="form-group">
                    <label for="num-months-saques">Número de Meses</label>
                    <input type="number" id="num-months-saques" value="10" required>
                </div>
                <div class="button-group">
                    <button type="button" class="btn btn-primary" onclick="calcularJuros()">Calcular Juros</button>
                    <button type="button" class="btn btn-secondary" onclick="limpar('saques-form')">Limpar</button>
                </div>
            </form>

            <div id="results-saques" style="display: none;">
                <div class="summary">
                    <h3>Resumo Final</h3>
                    <p class="final-balance">Saldo Final: <span id="final-balance-saques"></span></p>
                    <p class="total-juros">Juros Totais Acumulados: <span id="total-juros-saques"></span></p>
                </div>

                <h3>Log Detalhado Mês a Mês</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Mês</th>
                            <th>Saldo Inicial</th>
                            <th>Juros</th>
                            <th>Saldo Final</th>
                        </tr>
                    </thead>
                    <tbody id="monthly-log-body-saques">
                        </tbody>
                </table>
            </div>
        </div>

        <div id="tab-oportunidade" class="tab-content">
            <div class="cdi-card">
                <h4>Taxa de Juros de Referência (CDI)</h4>
                <p>Para obter o valor atual do CDI, consulte a taxa SELIC no site oficial do Banco Central. O CDI geralmente acompanha a SELIC de perto.</p>
                <a href="https://www.bcb.gov.br/" target="_blank">Consultar no site do Banco Central</a>
            </div>

            <form id="oportunidade-form">
                <div class="form-group">
                    <label for="initial-principal-oportunidade">Valor do Produto (R$)</label>
                    <input type="number" id="initial-principal-oportunidade" value="3000" step="0.01" required>
                </div>
                <div class="form-group">
                    <label for="monthly-withdrawal-oportunidade">Valor da Parcela (R$)</label>
                    <input type="number" id="monthly-withdrawal-oportunidade" value="300" step="0.01" required>
                </div>
                <div class="form-group">
                    <label for="discount-rate-oportunidade">Desconto à Vista (%)</label>
                    <input type="number" id="discount-rate-oportunidade" value="0" step="0.01" required>
                </div>
                <div class="form-group">
                    <div class="flex-row">
                        <label for="monthly-rate-oportunidade">Taxa Mensal (%)</label>
                        <input type="checkbox" id="use-cdi-oportunidade" onclick="toggleCdiRate('oportunidade')">
                        <label for="use-cdi-oportunidade" style="font-weight: normal; margin-left: 5px;">Usar 100% do CDI</label>
                    </div>
                    <input type="number" id="monthly-rate-oportunidade" value="1" step="0.01" required>
                </div>
                <div class="form-group" id="cdi-rate-group-oportunidade" style="display: none;">
                    <label for="cdi-annual-rate-oportunidade">Taxa Anual do CDI (%)</label>
                    <input type="number" id="cdi-annual-rate-oportunidade" value="10" step="0.01" required>
                </div>
                <div class="form-group">
                    <label for="num-months-oportunidade">Número de Meses</label>
                    <input type="number" id="num-months-oportunidade" value="10" required>
                </div>
                <div class="button-group">
                    <button type="button" class="btn btn-primary" onclick="analisarOportunidade()">Analisar Oportunidade</button>
                    <button type="button" class="btn btn-secondary" onclick="limpar('oportunidade-form')">Limpar</button>
                </div>
            </form>

            <div id="results-oportunidade" style="display: none;">
                <div class="comparison-card">
                    <h4>Análise Comparativa Final</h4>
                    <p>Ganho Total (Compra Parcelada): <span id="final-gain-parcelado"></span></p>
                    <p>Ganho Total (Compra à Vista): <span id="final-gain-vista"></span></p>
                    <p id="winner-message"></p>
                </div>

                <div class="chart-container">
                    <h3>Evolução dos Ganhos Acumulados</h3>
                    <canvas id="myChart"></canvas>
                </div>
            </div>
        </div>

        <div id="tab-explanation" class="tab-content">
            <div class="explanation">
                <h3>O Conceito: Custo de Oportunidade e Ganhos</h3>
                <p>Esta ferramenta vai além de um simples cálculo de juros. Ela ajuda a visualizar o **custo de oportunidade** de uma compra, ou seja, o que o seu dinheiro poderia estar rendendo se você fizesse uma escolha diferente. A análise se baseia nos **ganhos financeiros líquidos** de dois cenários:</p>
                <ul>
                    <li>**Ganho ao Parcelar:** O total de juros que você acumula no seu investimento inicial, mesmo que você use parte dele para pagar as parcelas do produto.</li>
                    <li>**Ganho ao Comprar à Vista:** O valor do desconto que você recebeu, somado aos juros que esse valor renderia se fosse investido.</li>
                </ul>

                <h4>Como Usar as Abas</h4>
                <ul>
                    <li>
                        <strong>Aba "Juros com Saques":</strong> Use esta aba para simular a evolução do seu dinheiro em um investimento, considerando retiradas mensais para o pagamento de contas ou parcelas. O resultado é o saldo final e os juros totais acumulados.
                    </li>
                    <li>
                        <strong>Aba "Custo de Oportunidade":</strong> Use esta aba para comparar diretamente as duas opções de compra (parcelada vs. à vista com desconto). O gráfico de **Evolução dos Ganhos Acumulados** mostra o crescimento financeiro em cada cenário. A linha que estiver **mais alta** no final é a que representa a decisão financeiramente mais vantajosa.
                    </li>
                </ul>
            </div>
        </div>
    </div>

    <script>
        // Variável global para armazenar a instância do gráfico, permitindo que ela seja destruída
        let myChartInstance = null;

        function formatarMoeda(valor) {
            return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(valor);
        }

        function showTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));

            document.getElementById(tabId).classList.add('active');
            event.target.classList.add('active');
        }

        function toggleCdiRate(tab) {
            const useCdiCheckbox = document.getElementById(`use-cdi-${tab}`);
            const monthlyRateInput = document.getElementById(`monthly-rate-${tab}`);
            const cdiRateGroup = document.getElementById(`cdi-rate-group-${tab}`);

            if (useCdiCheckbox.checked) {
                monthlyRateInput.disabled = true;
                monthlyRateInput.style.display = 'none';
                cdiRateGroup.style.display = 'block';
            } else {
                monthlyRateInput.disabled = false;
                monthlyRateInput.style.display = 'block';
                cdiRateGroup.style.display = 'none';
            }
        }

        function calcularJuros() {
            const initialPrincipal = parseFloat(document.getElementById('initial-principal-saques').value);
            const monthlyWithdrawal = parseFloat(document.getElementById('monthly-withdrawal-saques').value);
            let monthlyRate;
            const useCdi = document.getElementById('use-cdi-saques').checked;
            
            if (useCdi) {
                const cdiAnnualRate = parseFloat(document.getElementById('cdi-annual-rate-saques').value);
                if (isNaN(cdiAnnualRate)) {
                    alert("Por favor, insira um valor válido para a Taxa Anual do CDI.");
                    return;
                }
                monthlyRate = Math.pow(1 + (cdiAnnualRate / 100), 1/12) - 1;
            } else {
                monthlyRate = parseFloat(document.getElementById('monthly-rate-saques').value) / 100;
            }
            
            const numMonths = parseInt(document.getElementById('num-months-saques').value);

            if (isNaN(initialPrincipal) || isNaN(monthlyWithdrawal) || isNaN(monthlyRate) || isNaN(numMonths) || numMonths <= 0) {
                alert("Por favor, preencha todos os campos com valores válidos.");
                return;
            }

            let currentBalance = initialPrincipal;
            let totalInterest = 0;
            const logData = [];

            for (let mes = 1; mes <= numMonths; mes++) {
                const interestEarned = currentBalance * monthlyRate;
                totalInterest += interestEarned;
                currentBalance += interestEarned;
                currentBalance -= monthlyWithdrawal;
                
                logData.push({
                    month: mes,
                    initialBalance: currentBalance + monthlyWithdrawal - interestEarned,
                    interest: interestEarned,
                    finalBalance: currentBalance
                });
            }
            const finalBalance = currentBalance;

            document.getElementById('final-balance-saques').textContent = formatarMoeda(finalBalance);
            document.getElementById('total-juros-saques').textContent = formatarMoeda(totalInterest);

            const tableBody = document.getElementById('monthly-log-body-saques');
            tableBody.innerHTML = '';

            logData.forEach(data => {
                const row = tableBody.insertRow();
                row.insertCell(0).textContent = data.month;
                row.insertCell(1).textContent = formatarMoeda(data.initialBalance);
                row.insertCell(2).textContent = formatarMoeda(data.interest);
                row.insertCell(3).textContent = formatarMoeda(data.finalBalance);
            });
            
            document.getElementById('results-saques').style.display = 'block';
        }

        function analisarOportunidade() {
            const initialPrincipal = parseFloat(document.getElementById('initial-principal-oportunidade').value);
            const monthlyWithdrawal = parseFloat(document.getElementById('monthly-withdrawal-oportunidade').value);
            const discountRate = parseFloat(document.getElementById('discount-rate-oportunidade').value) / 100;
            let monthlyRate;
            const useCdi = document.getElementById('use-cdi-oportunidade').checked;
            
            if (useCdi) {
                const cdiAnnualRate = parseFloat(document.getElementById('cdi-annual-rate-oportunidade').value);
                if (isNaN(cdiAnnualRate)) {
                    alert("Por favor, insira um valor válido para a Taxa Anual do CDI.");
                    return;
                }
                monthlyRate = Math.pow(1 + (cdiAnnualRate / 100), 1/12) - 1;
            } else {
                monthlyRate = parseFloat(document.getElementById('monthly-rate-oportunidade').value) / 100;
            }
            
            const numMonths = parseInt(document.getElementById('num-months-oportunidade').value);

            if (isNaN(initialPrincipal) || isNaN(monthlyWithdrawal) || isNaN(monthlyRate) || isNaN(numMonths) || numMonths <= 0) {
                alert("Por favor, preencha todos os campos com valores válidos.");
                return;
            }

            let currentBalance = initialPrincipal;
            let totalInterestParcelado = 0;
            const chartLabels = ["Início"];
            const chartGanhosParcelado = [0];

            for (let mes = 1; mes <= numMonths; mes++) {
                const interestEarned = currentBalance * monthlyRate;
                totalInterestParcelado += interestEarned;
                currentBalance += interestEarned;
                currentBalance -= monthlyWithdrawal;
                chartLabels.push(`Mês ${mes}`);
                chartGanhosParcelado.push(totalInterestParcelado);
            }

            const discountedValue = initialPrincipal * discountRate;
            let currentGainVista = discountedValue;
            const chartGanhosVista = [0];

            chartGanhosVista.push(discountedValue);

            for (let mes = 1; mes <= numMonths; mes++) {
                currentGainVista = currentGainVista * (1 + monthlyRate);
                chartGanhosVista.push(currentGainVista);
            }
            
            if (myChartInstance) {
                myChartInstance.destroy();
            }

            const ctx = document.getElementById('myChart').getContext('2d');
            myChartInstance = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: chartLabels,
                    datasets: [
                        {
                            label: 'Ganhos Acumulados - Opção Parcelada',
                            data: chartGanhosParcelado,
                            borderColor: var(--primary-color),
                            backgroundColor: 'rgba(46, 134, 222, 0.1)',
                            borderWidth: 2,
                            pointBackgroundColor: var(--primary-color),
                            tension: 0.3
                        },
                        {
                            label: 'Ganhos Acumulados - Opção à Vista (com desconto)',
                            data: chartGanhosVista,
                            borderColor: var(--success-color),
                            backgroundColor: 'rgba(39, 174, 96, 0.1)',
                            borderWidth: 2,
                            pointBackgroundColor: var(--success-color),
                            tension: 0.3
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Ganhos Acumulados (R$)',
                                color: var(--text-dark)
                            },
                            grid: {
                                color: '#EAEAEA'
                            },
                            ticks: {
                                callback: function(value, index, values) {
                                    return formatarMoeda(value);
                                }
                            }
                        },
                        x: {
                            title: {
                                display: true,
                                text: 'Mês',
                                color: var(--text-dark)
                            },
                            grid: {
                                color: '#EAEAEA'
                            }
                        }
                    },
                    plugins: {
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    let label = context.dataset.label || '';
                                    if (label) {
                                        label += ': ';
                                    }
                                    label += formatarMoeda(context.parsed.y);
                                    return label;
                                }
                            }
                        }
                    }
                }
            });

            document.getElementById('final-gain-parcelado').textContent = formatarMoeda(totalInterestParcelado);
            document.getElementById('final-gain-vista').textContent = formatarMoeda(currentGainVista);

            const winnerMessage = document.getElementById('winner-message');
            if (totalInterestParcelado > currentGainVista) {
                winnerMessage.textContent = "A opção parcelada é mais vantajosa! ✨";
                winnerMessage.className = "winner";
            } else if (currentGainVista > totalInterestParcelado) {
                winnerMessage.textContent = "A opção à vista é mais vantajosa! 🎉";
                winnerMessage.className = "winner";
            } else {
                winnerMessage.textContent = "Ambas as opções têm o mesmo resultado final.";
                winnerMessage.className = "";
            }
            
            document.getElementById('results-oportunidade').style.display = 'block';
        }

        function limpar(formId) {
            document.getElementById(formId).reset();
            const resultsId = formId === 'saques-form' ? 'results-saques' : 'results-oportunidade';
            document.getElementById(resultsId).style.display = 'none';

            if (myChartInstance) {
                myChartInstance.destroy();
            }

            toggleCdiRate(formId === 'saques-form' ? 'saques' : 'oportunidade');
        }

        document.addEventListener('DOMContentLoaded', () => {
            toggleCdiRate('saques');
            toggleCdiRate('oportunidade');
        });
    </script>
</body>
</html>
"""

st.set_page_config(layout="wide")
st.components.v1.html(html_code, height=1000, scrolling=True)
