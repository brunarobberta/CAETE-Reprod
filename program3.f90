

program gerar_listas
  implicit none
  integer :: i
  real :: npp_pls(5), mass_seed(5), npp_rep(5)

  ! gerar lista1 com valores de 0.5 a 5
  do i = 1, 5
     npp_pls(i) = i * 0.5
  end do

    ! imprimir 
  write(*,*) 'npp_pls:'
  do i = 1, 5
     write(*,*) npp_pls(i)
  end do

  ! gerar lista2 com valores de 1 a 5
  do i = 1, 5
     mass_seed(i) = i
  end do

  ! imprimir 
  write(*,*) 'mass_seed:'
  do i = 1, 5
     write(*,*) mass_seed(i)
  end do

  ! gerar a nova lista com 90% subtraído de cada elemento da lista1, sendo o npp_rep
  do i = 1, 5
     npp_rep(i) = npp_pls(i) - (npp_pls(i) * 0.9)
  end do

  ! imprimir a nova lista
  write(*,*)
  write(*,*) 'Npp_rep:'
  do i = 1, 5
     write(*,*) npp_rep(i)
  end do

end program gerar_listas
