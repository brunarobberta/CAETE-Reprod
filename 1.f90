program lista_fortran

implicit none

real :: npp_pls(5), mass_seed(5), npp_rep(5), n_seed(5), seed_bank(5)
real :: adicao(10) = 0.0 ! vetor com adição a ser aplicada em cada tempo
integer :: i, j
logical :: is_time1

! repetir o código 10 vezes
do j = 1, 10

  ! determinar o tempo atual
  is_time1 = (j == 1)

  ! gerando a lista1 com valores de 0.5 a 5
  do i = 1, 5
    npp_pls(i) = 0.5*(i+1)
  end do

  ! gerando a lista2 com valores de 1 a 5
  do i = 1, 5
    mass_seed(i) = i
  end do

  ! tirando 90% de cada número da lista1
  npp_rep = npp_pls*0.1

  ! dividindo os números da npp_rep com os números da mass_seed
  ! com condição de que os números da npp_rep sejam maiores que 0
  do i = 1, 5
    if (npp_rep(i) > 0) then
      n_seed(i) = npp_rep(i) / mass_seed(i)
    else
      n_seed(i) = 0.0
    end if
  end do





  ! calculando os números da lista final deixando apenas 60% de cada item
  seed_bank = n_seed*0.6
  
  ! dividindo por 60% se é tempo 1, ou usando o valor de 60% mais a adição do tempo 1
  if (is_time1) then
  seed_bank = n_seed*0.6
  else
  seed_bank = (n_seed*0.6) + adicao(j)
  end if

  print*, 'adição', adicao


   ! arredondando todos os valores para duas casas decimais
  npp_pls = nint(npp_pls*100)/100.0
  mass_seed = nint(mass_seed*100)/100.0
  npp_rep = nint(npp_rep*100)/100.0
  n_seed = nint(n_seed*100)/100.0
  seed_bank = nint(seed_bank*100)/100.0
  
  ! garantindo que nenhum valor seja abaixo de 0
  npp_pls = max(npp_pls, 0.0)
  mass_seed = max(mass_seed, 0.0)
  npp_rep = max(npp_rep, 0.0)
  n_seed = max(n_seed, 0.0)
  seed_bank = max(seed_bank, 0.0)





  !write(*,*) 'seed_bank: ', seed_bank

end do

end program lista_fortran
