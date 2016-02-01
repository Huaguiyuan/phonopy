import numpy as np
from phonopy.cui.settings import Settings, ConfParser, fracval

class Phono3pySettings(Settings):
    def __init__(self):
        Settings.__init__(self)

        self._boundary_mfp = 1.0e6 # In micrometre. The default value is
                                   # just set to avoid divergence.
        self._coarse_mesh_shifts = None
        self._constant_averaged_pp_interaction = None
        self._create_displacements = False
        self._cutoff_fc3_distance = None
        self._cutoff_pair_distance = None
        self._frequency_scale_factor = None
        self._grid_addresses = None
        self._grid_points = None
        self._ion_clamped = False
        self._is_bterta = False
        self._is_gruneisen = False
        self._is_imag_self_energy = False
        self._is_isotope = False
        self._is_joint_dos = False
        self._is_lbte = False
        self._is_linewidth = False
        self._is_frequency_shift = False
        self._mass_variances = None
        self._max_freepath = None
        self._mesh_divisors = None
        self._no_kappa_stars = False
        self._read_amplitude = False
        self._read_collision = None
        self._read_gamma = False
        self._run_with_g = True
        self._phonon_supercell_matrix = None
        self._pinv_cutoff = 1.0e-8
        self._scattering_event_class = None # scattering event class 1 or 2
        self._temperatures = None
        self._average_pp_interaction = False
        self._write_amplitude = False
        self._write_collision = False
        self._write_gamma = False
        self._write_detailed_gamma = False
        
    def set_boundary_mfp(self, boundary_mfp):
        self._boundary_mfp = boundary_mfp

    def get_boundary_mfp(self):
        return self._boundary_mfp

    def set_coarse_mesh_shifts(self, coarse_mesh_shifts):
        self._coarse_mesh_shifts = coarse_mesh_shifts

    def get_coarse_mesh_shifts(self):
        return self._coarse_mesh_shifts

    def set_create_displacements(self, create_displacements):
        self._create_displacements = create_displacements

    def get_create_displacements(self):
        return self._create_displacements

    def set_constant_averaged_pp_interaction(self, ave_pp):
        self._constant_averaged_pp_interaction = ave_pp

    def get_constant_averaged_pp_interaction(self):
        return self._constant_averaged_pp_interaction

    def set_cutoff_fc3_distance(self, cutoff_fc3_distance):
        self._cutoff_fc3_distance = cutoff_fc3_distance

    def get_cutoff_fc3_distance(self):
        return self._cutoff_fc3_distance

    def set_cutoff_pair_distance(self, cutoff_pair_distance):
        self._cutoff_pair_distance = cutoff_pair_distance

    def get_cutoff_pair_distance(self):
        return self._cutoff_pair_distance

    def set_frequency_scale_factor(self, frequency_scale_factor):
        self._frequency_scale_factor = frequency_scale_factor

    def get_frequency_scale_factor(self):
        return self._frequency_scale_factor

    def set_grid_addresses(self, grid_addresses):
        self._grid_addresses = grid_addresses

    def get_grid_addresses(self):
        return self._grid_addresses

    def set_grid_points(self, grid_points):
        self._grid_points = grid_points

    def get_grid_points(self):
        return self._grid_points

    def set_ion_clamped(self, ion_clamped):
        self._ion_clamped = ion_clamped

    def get_ion_clamped(self):
        return self._ion_clamped

    def set_is_bterta(self, is_bterta):
        self._is_bterta = is_bterta

    def get_is_bterta(self):
        return self._is_bterta

    def set_is_gruneisen(self, is_gruneisen):
        self._is_gruneisen = is_gruneisen

    def get_is_gruneisen(self):
        return self._is_gruneisen

    def set_is_imag_self_energy(self, is_imag_self_energy):
        self._is_imag_self_energy = is_imag_self_energy

    def get_is_imag_self_energy(self):
        return self._is_imag_self_energy

    def set_is_isotope(self, is_isotope):
        self._is_isotope = is_isotope

    def get_is_isotope(self):
        return self._is_isotope

    def set_is_joint_dos(self, is_joint_dos):
        self._is_joint_dos = is_joint_dos

    def get_is_joint_dos(self):
        return self._is_joint_dos

    def set_is_lbte(self, is_lbte):
        self._is_lbte = is_lbte

    def get_is_lbte(self):
        return self._is_lbte

    def set_is_linewidth(self, is_linewidth):
        self._is_linewidth = is_linewidth

    def get_is_linewidth(self):
        return self._is_linewidth

    def set_is_frequency_shift(self, is_frequency_shift):
        self._is_frequency_shift = is_frequency_shift

    def get_is_frequency_shift(self):
        return self._is_frequency_shift

    def set_mass_variances(self, mass_variances):
        self._mass_variances = mass_variances

    def get_mass_variances(self):
        return self._mass_variances

    def set_max_freepath(self, max_freepath):
        self._max_freepath = max_freepath

    def get_max_freepath(self):
        return self._max_freepath

    def set_mesh_divisors(self, mesh_divisors):
        self._mesh_divisors = mesh_divisors

    def get_mesh_divisors(self):
        return self._mesh_divisors

    def set_no_kappa_stars(self, no_kappa_stars):
        self._no_kappa_stars = no_kappa_stars

    def get_no_kappa_stars(self):
        return self._no_kappa_stars

    def set_phonon_supercell_matrix(self, matrix):
        self._phonon_supercell_matrix = matrix

    def get_phonon_supercell_matrix(self):
        return self._phonon_supercell_matrix

    def set_pinv_cutoff(self, pinv_cutoff):
        self._pinv_cutoff = pinv_cutoff

    def get_pinv_cutoff(self):
        return self._pinv_cutoff

    def set_read_amplitude(self, read_amplitude):
        self._read_amplitude = read_amplitude

    def get_read_amplitude(self):
        return self._read_amplitude

    def set_read_collision(self, read_collision):
        self._read_collision = read_collision

    def get_read_collision(self):
        return self._read_collision

    def set_read_gamma(self, read_gamma):
        self._read_gamma = read_gamma

    def get_read_gamma(self):
        return self._read_gamma

    def set_run_with_g(self, run_with_g):
        self._run_with_g = run_with_g

    def get_run_with_g(self):
        return self._run_with_g

    def set_scattering_event_class(self, scattering_event_class):
        self._scattering_event_class = scattering_event_class

    def get_scattering_event_class(self):
        return self._scattering_event_class

    def set_temperatures(self, temperatures):
        self._temperatures = temperatures

    def get_temperatures(self):
        return self._temperatures

    def set_average_pp_interaction(self, average_pp_interaction):
        self._average_pp_interaction = average_pp_interaction

    def get_average_pp_interaction(self):
        return self._average_pp_interaction

    def set_write_amplitude(self, write_amplitude):
        self._write_amplitude = write_amplitude

    def get_write_amplitude(self):
        return self._write_amplitude

    def set_write_collision(self, write_collision):
        self._write_collision = write_collision

    def get_write_collision(self):
        return self._write_collision

    def set_write_detailed_gamma(self, write_detailed_gamma):
        self._write_detailed_gamma = write_detailed_gamma

    def get_write_detailed_gamma(self):
        return self._write_detailed_gamma

    def set_write_gamma(self, write_gamma):
        self._write_gamma = write_gamma

    def get_write_gamma(self):
        return self._write_gamma


class Phono3pyConfParser(ConfParser):
    def __init__(self, filename=None, options=None, option_list=None):
        ConfParser.__init__(self, filename, options, option_list)
        self._read_options()
        self._parse_conf()
        self._settings = Phono3pySettings()
        self._set_settings()

    def _read_options(self):
        for opt in self._option_list:
            if opt.dest == 'phonon_supercell_dimension':
                if self._options.phonon_supercell_dimension is not None:
                    self._confs['dim_fc2'] = self._options.phonon_supercell_dimension

            if opt.dest == 'boundary_mfp':
                if self._options.boundary_mfp is not None:
                    self._confs['boundary_mfp'] = self._options.boundary_mfp

            if opt.dest == 'constant_averaged_pp_interaction':
                if self._options.constant_averaged_pp_interaction is not None:
                    self._confs['constant_averaged_pp_interaction'] = self._options.constant_averaged_pp_interaction

            if opt.dest == 'cutoff_fc3_distance':
                if self._options.cutoff_fc3_distance is not None:
                    self._confs['cutoff_fc3_distance'] = self._options.cutoff_fc3_distance

            if opt.dest == 'cutoff_pair_distance':
                if self._options.cutoff_pair_distance is not None:
                    self._confs['cutoff_pair_distance'] = self._options.cutoff_pair_distance

            if opt.dest == 'frequency_scale_factor':
                if self._options.frequency_scale_factor is not None:
                    self._confs['frequency_scale_factor'] = self._options.frequency_scale_factor

            if opt.dest == 'grid_addresses':
                if self._options.grid_addresses is not None:
                    self._confs['grid_addresses'] = self._options.grid_addresses

            if opt.dest == 'grid_points':
                if self._options.grid_points is not None:
                    self._confs['grid_points'] = self._options.grid_points

            if opt.dest == 'ion_clamped':
                if self._options.ion_clamped:
                    self._confs['ion_clamped'] = '.true.'

            if opt.dest == 'is_bterta':
                if self._options.is_bterta:
                    self._confs['bterta'] = '.true.'

            if opt.dest == 'is_gruneisen':
                if self._options.is_gruneisen:
                    self._confs['gruneisen'] = '.true.'

            if opt.dest == 'is_displacement':
                if self._options.is_displacement:
                    self._confs['create_displacements'] = '.true.'

            if opt.dest == 'is_imag_self_energy':
                if self._options.is_imag_self_energy:
                    self._confs['imag_self_energy'] = '.true.'

            if opt.dest == 'is_isotope':
                if self._options.is_isotope:
                    self._confs['isotope'] = '.true.'

            if opt.dest == 'is_joint_dos':
                if self._options.is_joint_dos:
                    self._confs['joint_dos'] = '.true.'

            if opt.dest == 'is_lbte':
                if self._options.is_lbte:
                    self._confs['lbte'] = '.true.'

            if opt.dest == 'is_linewidth':
                if self._options.is_linewidth:
                    self._confs['linewidth'] = '.true.'

            if opt.dest == 'is_frequency_shift':
                if self._options.is_frequency_shift:
                    self._confs['frequency_shift'] = '.true.'

            if opt.dest == 'mass_variances':
                if self._options.mass_variances is not None:
                    self._confs['mass_variances'] = self._options.mass_variances

            if opt.dest == 'max_freepath':
                if self._options.max_freepath is not None:
                    self._confs['max_freepath'] = self._options.max_freepath

            if opt.dest == 'mesh_divisors':
                if self._options.mesh_divisors is not None:
                    self._confs['mesh_divisors'] = self._options.mesh_divisors

            if opt.dest == 'no_kappa_stars':
                if self._options.no_kappa_stars:
                    self._confs['no_kappa_stars'] = '.true.'

            if opt.dest == 'pinv_cutoff':
                if self._options.pinv_cutoff is not None:
                    self._confs['pinv_cutoff'] = self._options.pinv_cutoff

            if opt.dest == 'read_amplitude':
                if self._options.read_amplitude:
                    self._confs['read_amplitude'] = '.true.'

            if opt.dest == 'read_gamma':
                if self._options.read_gamma:
                    self._confs['read_gamma'] = '.true.'

            if opt.dest == 'run_with_g':
                if not self._options.run_with_g:
                    self._confs['run_with_g'] = '.false.'

            if opt.dest == 'read_collision':
                if self._options.read_collision is not None:
                    self._confs['read_collision'] = self._options.read_collision

            if opt.dest == 'scattering_event_class':
                if self._options.scattering_event_class is not None:
                    self._confs['scattering_event_class'] = self._options.scattering_event_class

            if opt.dest == 'temperatures':
                if self._options.temperatures is not None:
                    self._confs['temperatures'] = self._options.temperatures

            if opt.dest == 'average_pp_interaction':
                if self._options.average_pp_interaction:
                    self._confs['average_pp_interaction'] = '.true.'

            if opt.dest == 'write_amplitude':
                if self._options.write_amplitude:
                    self._confs['write_amplitude'] = '.true.'

            if opt.dest == 'write_detailed_gamma':
                if self._options.write_detailed_gamma:
                    self._confs['write_detailed_gamma'] = '.true.'

            if opt.dest == 'write_gamma':
                if self._options.write_gamma:
                    self._confs['write_gamma'] = '.true.'

            if opt.dest == 'write_collision':
                if self._options.write_collision:
                    self._confs['write_collision'] = '.true.'

    def _parse_conf(self):
        confs = self._confs

        for conf_key in confs.keys():
            if conf_key == 'create_displacements':
                if confs['create_displacements'] == '.true.':
                    self.set_parameter('create_displacements', True)

            if conf_key == 'dim_fc2':
                matrix = [ int(x) for x in confs['dim_fc2'].split() ]
                if len(matrix) == 9:
                    matrix = np.array(matrix).reshape(3, 3)
                elif len(matrix) == 3:
                    matrix = np.diag(matrix)
                else:
                    self.setting_error(
                        "Number of elements of dim2 has to be 3 or 9.")

                if matrix.shape == (3, 3):
                    if np.linalg.det(matrix) < 1:
                        self.setting_error(
                            "Determinant of supercell matrix has " +
                            "to be positive.")
                    else:
                        self.set_parameter('dim_fc2', matrix)

            if conf_key == 'boundary_mfp':
                self.set_parameter('boundary_mfp',
                                   float(confs['boundary_mfp']))

            if conf_key == 'constant_averaged_pp_interaction':
                self.set_parameter(
                    'constant_averaged_pp_interaction',
                    float(confs['constant_averaged_pp_interaction']))

            if conf_key == 'cutoff_fc3_distance':
                self.set_parameter('cutoff_fc3_distance',
                                   float(confs['cutoff_fc3_distance']))

            if conf_key == 'cutoff_pair_distance':
                self.set_parameter('cutoff_pair_distance',
                                   float(confs['cutoff_pair_distance']))

            if conf_key == 'frequency_scale_factor':
                self.set_parameter('frequency_scale_factor',
                                   float(confs['frequency_scale_factor']))

            if conf_key == 'grid_addresses':
                vals = [int(x) for x in
                        confs['grid_addresses'].replace(',', ' ').split()]
                if len(vals) % 3 == 0 and len(vals) > 0:
                    self.set_parameter('grid_addresses',
                                       np.reshape(vals, (-1, 3)))
                else:
                    self.setting_error("Grid addresses are incorrectly set.")


            if conf_key == 'grid_points':
                vals = [int(x) for x in
                        confs['grid_points'].replace(',', ' ').split()]
                self.set_parameter('grid_points', vals)

            if conf_key == 'ion_clamped':
                if confs['ion_clamped'] == '.true.':
                    self.set_parameter('ion_clamped', True)

            if conf_key == 'bterta':
                if confs['bterta'] == '.true.':
                    self.set_parameter('is_bterta', True)

            if conf_key == 'gruneisen':
                if confs['gruneisen'] == '.true.':
                    self.set_parameter('is_gruneisen', True)

            if conf_key == 'imag_self_energy':
                if confs['imag_self_energy'] == '.true.':
                    self.set_parameter('is_imag_self_energy', True)
                    
            if conf_key == 'isotope':
                if confs['isotope'] == '.true.':
                    self.set_parameter('is_isotope', True)
                    
            if conf_key == 'joint_dos':
                if confs['joint_dos'] == '.true.':
                    self.set_parameter('is_joint_dos', True)

            if conf_key == 'lbte':
                if confs['lbte'] == '.true.':
                    self.set_parameter('is_lbte', True)

            if conf_key == 'linewidth':
                if confs['linewidth'] == '.true.':
                    self.set_parameter('is_linewidth', True)

            if conf_key == 'frequency_shift':
                if confs['frequency_shift'] == '.true.':
                    self.set_parameter('is_frequency_shift', True)

            if conf_key == 'mass_variances':
                vals = [fracval(x) for x in confs['mass_variances'].split()]
                if len(vals) < 1:
                    self.setting_error("Mass variance parameters are incorrectly set.")
                else:
                    self.set_parameter('mass_variances', vals)

            if conf_key == 'max_freepath':
                self.set_parameter('max_freepath', float(confs['max_freepath']))

            if conf_key == 'mesh_divisors':
                vals = [x for x in confs['mesh_divisors'].split()]
                if len(vals) == 3:
                    self.set_parameter('mesh_divisors', [int(x) for x in vals])
                elif len(vals) == 6:
                    divs = [int(x) for x in vals[:3]]
                    is_shift = [x.lower() == 't' for x in vals[3:]]
                    for i in range(3):
                        if is_shift[i] and (divs[i] % 2 != 0):
                            is_shift[i] = False
                            self.setting_error("Coarse grid shift along the " +
                                               ["first", "second", "third"][i] +
                                               " axis is not allowed.")
                    self.set_parameter('mesh_divisors', divs + is_shift)
                else:
                    self.setting_error("Mesh divisors are incorrectly set.")

            if conf_key == 'no_kappa_stars':
                if confs['no_kappa_stars'] == '.true.':
                    self.set_parameter('no_kappa_stars', True)

            if conf_key == 'pinv_cutoff':
                self.set_parameter('pinv_cutoff', float(confs['pinv_cutoff']))

            if conf_key == 'read_amplitude':
                if confs['read_amplitude'] == '.true.':
                    self.set_parameter('read_amplitude', True)

            if conf_key == 'read_collision':
                if confs['read_collision'] == 'all':
                    self.set_parameter('read_collision', 'all')
                else:
                    vals = [int(x) for x in confs['read_collision'].split()]
                    self.set_parameter('read_collision', vals)

            if conf_key == 'read_gamma':
                if confs['read_gamma'] == '.true.':
                    self.set_parameter('read_gamma', True)

            if conf_key == 'run_with_g':
                if confs['run_with_g'] == '.false.':
                    self.set_parameter('run_with_g', False)

            if conf_key == 'scattering_event_class':
                self.set_parameter('scattering_event_class',
                                   confs['scattering_event_class'])

            if conf_key == 'temperatures':
                vals = [fracval(x) for x in confs['temperatures'].split()]
                if len(vals) < 1:
                    self.setting_error("Temperatures are incorrectly set.")
                else:
                    self.set_parameter('temperatures', vals)

            if conf_key == 'average_pp_interaction':
                if confs['average_pp_interaction'] == '.true.':
                    self.set_parameter('average_pp_interaction', True)

            if conf_key == 'write_amplitude':
                if confs['write_amplitude'] == '.true.':
                    self.set_parameter('write_amplitude', True)

            if conf_key == 'write_detailed_gamma':
                if confs['write_detailed_gamma'] == '.true.':
                    self.set_parameter('write_detailed_gamma', True)
                    
            if conf_key == 'write_gamma':
                if confs['write_gamma'] == '.true.':
                    self.set_parameter('write_gamma', True)

            if conf_key == 'write_collision':
                if confs['write_collision'] == '.true.':
                    self.set_parameter('write_collision', True)
                    

    def _set_settings(self):
        ConfParser.set_settings(self)
        params = self._parameters

        # Is getting least displacements?
        if 'create_displacements' in params:
            if params['create_displacements']:
                self._settings.set_create_displacements('displacements')
    
        # Supercell dimension for fc2
        if params.has_key('dim_fc2'):
            self._settings.set_phonon_supercell_matrix(params['dim_fc2'])

        # Boundary mean free path for thermal conductivity calculation
        if params.has_key('boundary_mfp'):
            self._settings.set_boundary_mfp(params['boundary_mfp'])

        # Peierls type approximation for squared ph-ph interaction strength
        if params.has_key('constant_averaged_pp_interaction'):
            self._settings.set_constant_averaged_pp_interaction(
                params['constant_averaged_pp_interaction'])

        # Cutoff distance of third-order force constants. Elements where any 
        # pair of atoms has larger distance than cut-off distance are set zero.
        if params.has_key('cutoff_fc3_distance'):
            self._settings.set_cutoff_fc3_distance(params['cutoff_fc3_distance'])

        # Cutoff distance between pairs of displaced atoms used for supercell
        # creation with displacements and making third-order force constants
        if params.has_key('cutoff_pair_distance'):
            self._settings.set_cutoff_pair_distance(
                params['cutoff_pair_distance'])

        # This scale factor is multiplied to frequencies only, i.e., changes 
        # frequencies but assumed not to change the physical unit
        if params.has_key('frequency_scale_factor'):
            self._settings.set_frequency_scale_factor(
                params['frequency_scale_factor'])

        # Grid addresses (sets of three integer values)
        if params.has_key('grid_addresses'):
            self._settings.set_grid_addresses(params['grid_addresses'])

        # Grid points
        if params.has_key('grid_points'):
            self._settings.set_grid_points(params['grid_points'])

        # Atoms are clamped under applied strain in Gruneisen parameter calculation
        if params.has_key('ion_clamped'):
            self._settings.set_ion_clamped(params['ion_clamped'])

        # Calculate thermal conductivity in BTE-RTA
        if params.has_key('is_bterta'):
            self._settings.set_is_bterta(params['is_bterta'])

        # Calculate phonon-Gruneisen parameters
        if params.has_key('is_gruneisen'):
            self._settings.set_is_gruneisen(params['is_gruneisen'])

        # Calculate imaginary part of self energy
        if params.has_key('is_imag_self_energy'):
            self._settings.set_is_imag_self_energy(params['is_imag_self_energy'])

        # Calculate lifetime due to isotope scattering
        if params.has_key('is_isotope'):
            self._settings.set_is_isotope(params['is_isotope'])

        # Calculate joint-DOS
        if params.has_key('is_joint_dos'):
            self._settings.set_is_joint_dos(params['is_joint_dos'])

        # Calculate thermal conductivity in LBTE with Chaput's method
        if params.has_key('is_lbte'):
            self._settings.set_is_lbte(params['is_lbte'])

        # Calculate linewidths
        if params.has_key('is_linewidth'):
            self._settings.set_is_linewidth(params['is_linewidth'])

        # Calculate frequency_shifts
        if params.has_key('is_frequency_shift'):
            self._settings.set_is_frequency_shift(params['is_frequency_shift'])

        # Mass variance parameters
        if params.has_key('mass_variances'):
            self._settings.set_mass_variances(params['mass_variances'])

        # Maximum mean free path
        if params.has_key('max_freepath'):
            self._settings.set_max_freepath(params['max_freepath'])

        # Divisors for mesh numbers
        if params.has_key('mesh_divisors'):
            self._settings.set_mesh_divisors(params['mesh_divisors'][:3])
            if len(params['mesh_divisors']) > 3:
                self._settings.set_coarse_mesh_shifts(
                    params['mesh_divisors'][3:])

        # Cutoff frequency for pseudo inversion of collision matrix
        if params.has_key('pinv_cutoff'):
            self._settings.set_pinv_cutoff(params['pinv_cutoff'])

        # Read phonon-phonon interaction amplitudes from hdf5
        if params.has_key('read_amplitude'):
            self._settings.set_read_amplitude(params['read_amplitude'])

        # Read collision matrix and gammas from hdf5
        if params.has_key('read_collision'):
            self._settings.set_read_collision(params['read_collision'])

        # Read gammas from hdf5
        if params.has_key('read_gamma'):
            self._settings.set_read_gamma(params['read_gamma'])
            
        # Calculate imag-part self energy with integration weights from gaussian
        # smearing function
        if params.has_key('run_with_g'):
            self._settings.set_run_with_g(params['run_with_g'])
            
        # Sum partial kappa at q-stars
        if params.has_key('no_kappa_stars'):
            self._settings.set_no_kappa_stars(params['no_kappa_stars'])

        # Scattering event class 1 or 2
        if params.has_key('scattering_event_class'):
            self._settings.set_scattering_event_class(
                params['scattering_event_class'])

        # Temperatures
        if params.has_key('temperatures'):
            self._settings.set_temperatures(params['temperatures'])

        # Use averaged ph-ph interaction
        if params.has_key('average_pp_interaction'):
            self._settings.set_average_pp_interaction(
                params['average_pp_interaction'])

        # Write phonon-phonon interaction amplitudes to hdf5
        if params.has_key('write_amplitude'):
            self._settings.set_write_amplitude(params['write_amplitude'])

        # Write detailed imag-part of self energy to hdf5
        if params.has_key('write_detailed_gamma'):
            self._settings.set_write_detailed_gamma(
                params['write_detailed_gamma'])

        # Write imag-part of self energy to hdf5
        if params.has_key('write_gamma'):
            self._settings.set_write_gamma(params['write_gamma'])

        # Write collision matrix and gammas to hdf5
        if params.has_key('write_collision'):
            self._settings.set_write_collision(params['write_collision'])
            

        

