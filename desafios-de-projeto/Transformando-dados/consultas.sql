-- CONSULTAS:

-- Mesclar consultas employee e departament para criar uma tabela employee com o nome dos departamentos associados aos colaboradores.
-- A mescla terá como base a tabela employee.
CREATE TABLE employee_with_departaments AS
SELECT e.*, d.Dname AS Dept_name
FROM employee e
INNER JOIN departament d ON e.Dno = d.Dnumber;

-- Mescle os nomes de departamentos e localizações para criar uma tabela que associa cada combinação departamento-local a uma entrada única.
SELECT d.Dname, dl.Dlocation FROM departament d
INNER JOIN dept_locations dl ON d.Dnumber = dl.Dnumber;

-- Realize a junção dos colaboradores e respectivos nomes dos gerentes.
SELECT CONCAT(e.Fname, ' ', e.Lname) AS Full_Name, m.Fname
FROM employee e
INNER JOIN employee m ON e.Super_ssn = m.Ssn;

-- Agrupe os dados a fim de saber quantos colaboradores existem por gerente.
SELECT CONCAT(m.Fname, ' ', m.Lname) AS Manager_Name, COUNT(*) AS Number_of_employees
FROM employee e
INNER JOIN employee m ON e.Super_ssn = m.Ssn
GROUP BY m.Fname;