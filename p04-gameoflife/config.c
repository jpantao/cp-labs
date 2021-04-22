/*
 * Copyright (C) 2009 Raphael Kubo da Costa <kubito@gmail.com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "config.h"
#include "mem.h"


/* Error messages */
static const char *const unknown_optional_message = "Unknown optional flag";
static const char *const usage_message = "\nConway's Game of Life"
                                         "\nRaphael Kubo da Costa, RA 072201"
                                         "\n"
                                         "\nUsage: p04_gameoflife GENERATIONS INPUT_FILE [OPTIONS]"
                                         "\n"
                                         "\n  GENERATIONS is the number of generations the game should run"
                                         "\n  INPUT_FILE  is a file containing an initial board state"
                                         "\n"
                                         "\n  OPTIONS:"
                                         "\n  -p <pause>\tpause is the value in ms to wait before printing each generation"
                                         "\n  -q\t\tquiet mode (only print last frame)"
                                         "\n"
                                         "\n";

void game_config_free(GameConfig *config) {
    if (config) {
        fclose(config->input_file);
        free(config);
    }
}

size_t game_config_get_generations(GameConfig *config) {
    assert(config);
    return config->generations;
}

GameConfig *game_config_new_from_cli(int argc, char *argv[]) {
    char *endptr;
    FILE *file;
    GameConfig *config;
    long generations;

    if (argc < CLI_ARGC) {
        fprintf(stderr, "%s", usage_message);
        return NULL;
    }

    generations = strtol(argv[1], &endptr, 10);
    if ((*endptr != '\0') || (generations < 0)) {
        fprintf(stderr, "Error: GENERATIONS must be a valid positive integer\n");
        return NULL;
    }

    file = fopen(argv[2], "r");
    if (!file) {
        fprintf(stderr, "Error: could not open '%s'\n", argv[2]);
        return NULL;
    }

    config = MEM_ALLOC(GameConfig);
    config->n_threads = DEFAULT_N_THREADS;
    config->quiet_mode = DEFAULT_QUIET_MODE;
    config->pause = DEFAULT_FRAME_RATE;
    config->generations = (size_t) generations;
    config->input_file = file;

    //handle optional argument
    if (argc - CLI_ARGC > 0)
        for (int i = CLI_ARGC; i < argc; i++){
            char  *ptr;
            if (argv[i][0] == '-')
                switch (argv[i][1]) {
                    case 'p':
                        if ((config->pause = (int) strtol(argv[++i], &ptr, 10)) != 0
                            || strlen(argv[i]) <= 1)
                            break;
                        fprintf(stderr, "Value %s is not an number\n", argv[i]);
                        return NULL;
                    case 'q':
                        config->quiet_mode = 1; //True
                        break;
                    case 't':
                        if ((config->n_threads = (int) strtol(argv[++i], &ptr, 10)) != 0
                            || strlen(argv[i]) <= 1)
                            break;
                        fprintf(stderr, "Value %s is not an number\n", argv[i]);
                        return NULL;
                        break;
                    default:
                        fprintf(stderr, "%s \"%s\" ignoring...\n", unknown_optional_message, argv[i++]);
                }
        }


    return config;
}
