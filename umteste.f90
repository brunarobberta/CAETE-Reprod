program lista_numeros
    implicit none
    
    !real :: npp_pls(5), mass_seed(5), npp_rep(5)
    !real :: a, b
    !integer :: i
    

    real :: npp_pls(5), mass_seed(5), npp_rep(5)
    real :: valor, intervalo
    integer :: i
    
    valor = 1 ! valor inicial do intervalo
    intervalo = (5.0 - valor) / 4.0 ! intervalo entre cada valor
    
    do i = 1, 5
        npp_pls(i) = valor
        valor = valor + intervalo ! atualiza o valor para o próximo elemento da lista
        write(*,*) npp_pls(i)
    end do


    do i = 1, 5
        npp_rep(i) = npp_pls(i) * 0.1 ! reduz o valor em 90%
        write(*,*) npp_rep(i)
    end do
    
end program lista_numeros






