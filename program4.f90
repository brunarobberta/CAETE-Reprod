program lista_fortran

implicit none

real :: npp_pls(5), mass_seed(5), npp_rep(5), n_seed(5)
integer :: i

! gerando a npp_pls com valores de 0.5 a 5
do i = 1, 5
  npp_pls(i) = 0.5*(i+1)
end do

! gerando a mass_seed com valores de 1 a 5
do i = 1, 5
  mass_seed(i) = i
end do

! tirando 90% de cada número da lista1
npp_rep = npp_pls*0.1

! dividindo os números da mass_seed com os números da npp_rep
!n_seed = npp_rep / mass_seed

! dividindo os números da mass_seed com os números da npp_rep
! com condição de que os números da npp_rep sejam maiores que 0
do i = 1, 5
  if (npp_rep(i) > 0) then
    n_seed = npp_rep / mass_seed(i)
  else
    n_seed = 0.0
  end if
end do


! exibindo o resultado final
write(*,*) 'npp_pls: ', npp_pls
write(*,*) 'mass_seed: ', mass_seed
write(*,*) 'npp_rep (após tirar 90%): ', npp_rep
write(*,*) 'n_seed (após a divisão): ', n_seed

end program lista_fortran
