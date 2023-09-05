program test_1
    implicit none
    use types

!variando declaraveis 

    integer (i_8), parameter :: pls = 5 !parametro: pq determina a dimensão das outras variaveis
    integer (i_8), parameter :: time = 10
    real (r_8), dimension (pls) :: npp_pls !em gramas
    real (r_8), dimension (pls) :: seed_mass !em gramas
    real (r_8), dimension (pls) :: npp_rep
    integer (i_4), dimension (pls) :: n_seed
    integer (i_4):: seed_bank
    integer ::p,j

    !listas arrays

    npp_pls = (/2.5, 3.3, 3., 4.4, 5./)
    seed_mass = (/0.2, 0.4, 0.7, 0.8, 1./)



    do j = 1, time
    do p = 1, pls
    npp_re (p) 



    end program test_1