
public = (establishment,shrink) 


def establishment: (j,gc_available,npls_alive, FPC_total_accu_2, gc_area, est, est_pls,dens):
    
integer, intent(in) = j
    real, intent(in) :: npls_alive
    real, intent(in) :: FPC_total_accu_2
    real, intent(in) :: gc_area
    real, intent(in) :: gc_available
    real, intent(in) :: dens
    

    !output variables
    real, intent(out):: est
    real, intent(out):: est_pls
    
    !internal variables
    real :: est_max  !2 individuals m -2 yr -1 - reference: Levis et al 2004 (Eq 53)
    real :: FPC_total_perc
    ! print*, 'alive pls in est', npls
    real, parameter :: dens_min = 1.e-10      !minimum individual density for persistence of PFT (indiv/m2)
    
    
    ! if (dens.le.dens_min) then
    !     print*, 'DENS MIN', dens, j
    ! endif

    est_max = 4 *(gc_available)
    ! print*, est_max
    ! est_max = 2*(gc_area)
    FPC_total_perc = FPC_total_accu_2/gc_area
        
        ! print*, 'fpc perc', FPC_total_perc
    !lpjmlfire
    est = est_max * (1. - exp(5. * (FPC_total_perc- 1.))) / npls_alive
    ! print*, 'testing lpjfire est',est, npls_alive, est_max


    ! if(FPC_total_perc.lt.0.9) then
    !     !smith
    !     est = 0.06*(1-FPC_total_perc)



    ! !     est = est_max*(1 - FPC_total_perc)
    ! !     ! print*, 'lt 0.9'
    ! else
    !     !smith
    !     est = 0.06*(1-exp(-5*(1-FPC_total_perc)))*(1-FPC_total_perc)

    ! !     est = est_max*(1 - exp(-5. * (1 - FPC_total_perc)))*(1 - FPC_total_perc)
    ! !     ! print*, 'gt 0.9'

    ! endif
    ! ! print*, 'testing current est',est
     
    !lpjmlfire
    est_pls = max(est * (1. - FPC_total_perc),0.)
        ! ! print*, 'testing lpjfire est pls',est_pls


    !smith
    ! est_pls = est*(est_max/est_max*npls_alive)*FPC_total_perc*(1-FPC_total_perc)

    ! est_pls = est/npls_alive
        ! print*, 'testing cuurent est pls',est_pls
        

        ! print*, 'estab', est, est_pls, npls
    
    end subroutine

    subroutine shrink(cl_old,ch_old,cs_old,cw_old,cr_old,est_pls,dens_old,cleaf_sapl_npls,csap_sapl_npls,&
    &           cheart_sapl_npls,croot_sapl_npls, dens_new, cleaf_new,& 
    &           cwood_new,cheart_new, csap_new, croot_new)
    
        ! !input variables
        ! integer, intent(in) :: npls
        real, intent(in) :: cl_old
        real, intent(in) :: cw_old
        real, intent(in) :: ch_old
        real, intent(in) :: cs_old
        real, intent(in) :: cr_old
        real, intent(in) :: est_pls
        real, intent(in) :: dens_old
        real, intent(in) :: cleaf_sapl_npls
        real, intent(in) :: csap_sapl_npls
        real, intent(in) :: cheart_sapl_npls
        real, intent(in) :: croot_sapl_npls

        ! !output variables
        real, intent(out):: dens_new
        real, intent(out):: cleaf_new
        real, intent(out):: cwood_new
        real, intent(out):: cheart_new
        real, intent(out):: csap_new
        real, intent(out):: croot_new
        
        ! !internal variables
        ! real :: dens_est_pls 
        
        real :: cwood_sapl_npls
        
        
        if(cl_old.le.0.)then
            dens_new = 0.
            cleaf_new = 0.
            cheart_new = 0.
            csap_new = 0.
            cwood_sapl_npls = 0.
            cwood_new = 0.
            croot_new = 0.
        else
            dens_new = dens_old + est_pls


        ! print*, dens_new, dens_old 

        ! print*, 'dens_new', dens_new, 'dens_old', dens_old

            cleaf_new = ((cl_old*dens_old)+(cleaf_sapl_npls*est_pls))/dens_new
        ! print*,'cleaf_new',cleaf_new,'cl_old', cl_old, 'dens_olds', dens_old,'cleaf_sapl',cleaf_sapl_npls

            cheart_new = ((ch_old*dens_old)+(cheart_sapl_npls*est_pls))/dens_new

            csap_new = ((cs_old*dens_old)+(csap_sapl_npls*est_pls))/dens_new

            cwood_sapl_npls = csap_sapl_npls + cheart_sapl_npls
        ! print*, 'cwood_sapl', cwood_sapl_npls, 'est_pls',est_pls, cwood_sapl_npls*est_pls

            cwood_new = ((cw_old*dens_old)+(cwood_sapl_npls*est_pls))/dens_new
        ! print*,'cw_new',cwood_new/1000.,'cw_old', cw_old/1000.


            croot_new = ((cr_old*dens_old)+(croot_sapl_npls*est_pls))/dens_new
        ! print*, 'cr new', croot_new/1000., 'crold', cr_old/1000.
        endif
        
    end subroutine shrink

    subroutine sapling_allometry(npls_alive,cleaf_sapl_npls, csap_sapl_npls, cheart_sapl_npls,croot_sapl_npls)
        !subroutine to calculate carbon in saplings compartments

        !input variables
        real, intent(in) :: npls_alive
        
        ! !output variables
        real, intent(out) :: cleaf_sapl_npls     
        real, intent(out) :: csap_sapl_npls
        real, intent(out) :: cheart_sapl_npls
        real, intent(out) :: croot_sapl_npls

        real :: cleaf_sapl !gC
        real :: csap_sapl  !gC
        real :: cheart_sapl !gC
        real :: croot_sapl   !gC


        !internal variables
       

        real :: sla_sapl, diam_sapl, lai_sapl, height_sapl,dwood_sapl

        real :: klatosa_sapl = 8000.

        real :: pi = 3.14159

        real :: k_allom1_sapl = 100.

        real :: k_allom2_sapl = 40.

        real :: k_allom3_sapl = 0.5

        real :: x_sapl = 3. !from lpjlmfire (pftparametersmod.f90)

        real :: reinickerp = 1.6
        

       
        sla_sapl = 0.021 !from lpjlmfire (pftparametersmod.f90, line 229) m2/gC
        lai_sapl = 4 !lpjmlfire (pft parameter)
        dwood_sapl = 2e5 !gc/m3

        cleaf_sapl = (lai_sapl * k_allom1_sapl * x_sapl**reinickerp * (4. *sla_sapl / pi / klatosa_sapl)**(reinickerp * 0.5) / & 
                      sla_sapl)**(1. - 1. / reinickerp)  
        !print*, 'cleafsapl, lpjmlfire', cleaf_sapl

        diam_sapl = x_sapl * (4. * cleaf_sapl * sla_sapl / pi / klatosa_sapl)**0.5

        !print*, 'diamsapl, lpjmlfire', diam_sapl*100

        height_sapl = k_allom2_sapl*diam_sapl**k_allom3_sapl
        !print*, 'height, lpjmlfire', height_sapl

        csap_sapl = dwood_sapl * height_sapl * cleaf_sapl * sla_sapl / klatosa_sapl
        !print*, 'csapl, lpjmlfire', csap_sapl

        cheart_sapl = (x_sapl - 1.) * csap_sapl
        ! print*, 'cheart, lpjmlfire', cheart_sapl
        

        !update to gC and to distribution to the pls's

        !cleaf_sapl_npls = (cleaf_sapl*1000)/npls_alive
        !csap_sapl_npls = (csap_sapl*1000)/npls_alive
        !cheart_sapl_npls = (cheart_sapl*1000)/npls_alive
        !croot_sapl_npls = (croot_sapl*1000)/npls_alive

        cleaf_sapl_npls  = cleaf_sapl
        csap_sapl_npls   = csap_sapl
        cheart_sapl_npls = cheart_sapl
        croot_sapl_npls  = croot_sapl



        ! print*, cleaf_sapl_npls, csap_sapl_npls, cheart_sapl_npls, croot_sapl_npls


    end subroutine sapling_allometry

end module establish