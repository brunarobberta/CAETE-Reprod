!esse
program duas_listas
    implicit none
    !(r,8) p informar o pc quantas casas decimais tem, 64bits
    
    real :: npp_pls(5), mass_seed(5), npp_rep(5), n_seed(5), seed_bank(5)
    real :: valor1, intervalo1, valor2, intervalo2
    integer :: i, j

    npp_inicial = [/1.5, 2.5, 2., 3.5, 1./]

    ! repetir o código 10 vezes
    do p = 1,5 !NUMERO DE PLS
      do j = 1, 10 !time-step
    
    valor1 = 0.5 ! valor inicial do intervalo da npp_pls !em gramas
    intervalo1 = (5.0 - valor1) / 5.0 ! intervalo entre cada valor da npp_pls
    
    write(*,*) "npp_pls:"
    do i = 1, 5
        npp_pls(i) = valor1
        valor1 = valor1 + intervalo1 ! atualiza o valor para o próximo elemento da npp_pls
        write(*,*) npp_pls(i)
    end do
    
    write(*,*) 'npp_rep:'
    do i = 1, 5
        npp_rep(i) = npp_pls(i) * 0.1 ! reduz o valor em 90%
        write(*,*) npp_rep(i)
    end do
!    write(*,*)
    
    valor2 = 1.0 ! valor inicial do intervalo da mass_seed
    intervalo2 = 1.0 ! intervalo entre cada valor da mass_seed
    
    write(*,*) "mass_seed:"
    do i = 1, 5
        mass_seed(i) = valor2
        valor2 = valor2 + intervalo2 ! atualiza o valor para o próximo elemento da lista2
        write(*,*) mass_seed(i)
    end do
    
    write(*,*) "n_seed:"
    do i = 1, 5
  if (npp_rep(i) > 0) then
    n_seed = npp_rep / mass_seed(i)
  else
    n_seed = 0.0
  end if
  write(*,*) n_seed(i)
end do

    write(*,*) 'seed_bank:'
    do i = 1, 5
        seed_bank(i) = n_seed(i) * 0.6 ! reduz o valor em 60%
        write(*,*) n_seed(i)
    end do
    
    
    
    end program duas_listas
