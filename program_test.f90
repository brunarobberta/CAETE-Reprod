 program test
   implicit none
   
   integer :: i, n
   real :: npp_pls(5), mass_seed(5), npp_rep(5)
   real :: a, b
   
!   n = size(npp_pls)  ! Define o tamanho da lista de números gerados

  
  
  !!!! gerando numeros aleatorios de npp_pls e mass_seed
   call random_seed() ! inicializa o gerador de números aleatórios
   a = 0.5 ! limite inferior
   b = 5.0 ! limite superior
   
   do i = 1, 5
      call random_number(npp_pls(i))
      npp_pls(i) = a + (b-a)*npp_pls(i) ! escala para o intervalo desejado
   end do
   
   ! imprime os números gerados
   write(*,*) "npp_pls:"
   do i = 1, 5
    write(*,*) npp_pls(i)
   end do

   !removendo 10% do npp_pls para npp_rep
    do i = 1, 5
        npp_rep(i) = npp_pls(i) * 0.1 ! reduz o valor em 90%
        write(*,*) npp_rep(i)
    end do

  ! imprime os números gerados
   print*, "npp_rep:"
   do i = 1, 5
   print*, npp_rep(i)
   end do

   do i = 1, 5
      call random_number(mass_seed(i))
      mass_seed(i) = a + (b-a)*mass_seed(i) ! escala para o intervalo desejado
   end do
   
   ! imprime os números gerados
   print*, "mass_seed:"
   do i = 1, 5
   print*, mass_seed(i)
   end do




end program test