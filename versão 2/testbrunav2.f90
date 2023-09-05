module types
    implicit none
 
    ! FOR THE GNU FORTRAN COMPILER
    integer,parameter,public :: l_1 = 2  ! standart Logical type
    integer,parameter,public :: i_2 = 2  ! 16 bits integer
    integer,parameter,public :: i_4 = 4  ! 32 bits integer
    integer,parameter,public :: r_4 = 4  ! 32 bits float
    integer,parameter,public :: r_8 = 8  ! 64 bits float
 
end module types

program testbruna
    use types

    !VARIABLES DECLARATION

    integer(i_4), parameter :: pls = 5
    integer(i_4), parameter :: time = 10
    real(r_8), dimension(pls) :: npp_pls !quilogramas
    real(r_8), dimension(pls) :: seed_mass !gramas - trait variant
    real(r_8), dimension(pls) :: npp_rep !gramas
    integer(i_4), dimension(pls) :: n_seed
    integer(i_4), dimension(pls,time) :: seed_bank !banco de sementes
    integer(i_4), dimension(pls) :: seed_ok !60% DO NUMERO DE SEMENTES QUE SÃO VIAVEIS
    integer(i_4), dimension(pls) :: germ
    integer(i_4), dimension(time) :: water_soil !porcentagem de umidade no solo determinante da germinação
    integer(i_4), dimension(pls) :: lit
    integer :: p, j

    !ARRAYS - INICIAL (lista de valores iniciais para teste da lógica)

    npp_pls =(/2.5, 3.5, 2., 1.5, 1./)
    seed_mass =(/0.2, 3., 0.4, 0.7, 0.6/)
    water_soil =(/10,20,50,40,30,15,10,60,75,32/)

    !INICIO DA LÓGICA DE REPRODUÇÃO

    do j = 1, time !Loop de tempo - 10 anos.
        do p = 1,pls !Loop de PLS - 5 PLS total.

            !ETAPA 1 - Atribuir 10% da npp para a produção de sementes
            npp_rep(p) = (npp_pls(p)*1.D3)*0.1 
            
            !ETAPA 2 
            n_seed(p) = int(npp_rep(p)/seed_mass(p))

            !etapa 3
            write(*,*) "seed_bank:"
            seed_bank(p,j) = n_seed(p)
            write(*,*) seed_bank
            !seed_ok(p) = int(n_seed(p) * 0.6) !retira 40% das sementes do banco de sementes

            !etapa 4

            !fazer teste anual de viabilidade
            !ETAPA 4
            !CRIAR NUMEROS ALEATORIOS E, SE O VALOR DEFINIDO POR NOS Q O N ALEATRIO, ESSE E VIAVEL
            !IF SE N ALEA MENOR Q VALOR 0,7 A SEMENTE E VIAVEL

            !ETAPA 3/4 - DETERMINAÇÃO E ATUALIZAÇÃO SEED BANK será o novo 'teste de viabilidade'
            !probabilidade aleatoria de cada semente ser viavel ou n
            !as viaveis vao p passo 4: banco de sementes e depois aplica o calculo 5
            !nao viaveis vao p passo 6: tudo reincorporado na litera
            !etapa 3 e 4 em uma so: atualização e teste de viabilidade

            !mudar aqui para probabilidade de ser viavel ou n antes de germinar
            if (j .eq. 1) then 
                seed_bank(p,j) = seed_ok(p) !determinando o seed_bank - 60% das sementes viaveis (seed_ok)
            else
                seed_bank(p,j) = seed_ok(p) + seed_bank(p,j-1) !atualizando seed_bank [sintaxe 'j-1' -> pega ano anterior]
            endif

            !ETAPA 5 - GERMINAÇÃO (dependente da umidade disponível no solo em %)
            !e aqui mudaria p probabilidade de ser viavel e n de germinação, 
            !germinação seria depois
            !as que germinam vao pra alocação ou estabelecimento: codigo das meninas, ver isso se ha teste de estalecimento
            !será com base em relação a massa da semente
            if (water_soil(j) .gt. 30 .and. water_soil(j) .lt. 50) then
                germ(p) = (seed_ok(p) + seed_bank(p,j)) !100% de germinação - faixa ótima de umidade
            else
                germ(p) = int((seed_ok(p) + seed_bank(p,j)) * 0.2) !20% de germinação
            endif

            !ETAPA 6 - 40% das sementes produzidas são enviadas para a liteira do PLS
            lit(p) = int(n_seed(p) - seed_ok(p))
            
            !ETAPA 7 - Adicionar biomassa das germinadas no pool da PLS. como incorporar novas mudinhas a densidade do PLS que ja existe
            ! primeiro aumenta a densidade do PLS, 
            !ir pro looping de alocação das meninas?

        enddo
    enddo



end program testbruna